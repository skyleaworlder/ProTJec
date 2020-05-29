from .. import db_result
import pymysql
from . import baseSelect


def checkExistById(id, tableName):
    record_names = ("id")
    sql = 'SELECT id FROM ' + tableName + ' WHERE id = %s'
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (id,))
    )
    return DR

def checkExistByUsrNo(no):
    record_names = ("id")
    sql = 'SELECT id FROM users WHERE usr_no = %s'
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (no,))
    )
    return DR

def checkResExistByIds(usr_id, pro_id):
    record_names = ("state")
    sql = 'SELECT rsp_state FROM response WHERE usr_id = %s AND pro_id = %s'
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (usr_id, pro_id,))
    )
    return DR


def getPwdByNo(usr_no):
    record_names = ("password")
    sql = '''
        SELECT usr_password FROM users
        WHERE usr_no = %s
    '''
    DR = db_result.DbResult(
        record_names,
        baseSelect(sql, (usr_no,))
    )
    return DR



def getLoginLogs(usr_id, limit, offset):
    sql = '''
        SELECT lgi_time, '用户登录' FROM loginLogs
        WHERE usr_id = %s
        ORDER BY lgi_time DESC
        LIMIT %s OFFSET %s
    '''
    record_names = ("time", "comment")
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (usr_id, limit, offset,))
    )
    return DR



def getUsrInfoByNo(usr_no):
    record_names = (
        "id", "no", "name", "level", "inst",
        "grade", "avatar", "document", "chat"
    )
    sql = '''
        SELECT id, usr_no, usr_name, usr_userlevel, usr_inst,
                usr_grade, usr_avatar, usr_document, usr_chat
        FROM users
        WHERE usr_no = %s
    '''
    DR = db_result.DbResult(
        record_names,
        baseSelect(sql, (usr_no,))
    )
    return DR



def getUsrInfoById(usr_id):
    record_names = (
        "id", "no", "name", "level", "inst",
        "grade", "avatar", "document", "chat"
    )
    sql = '''
        SELECT id, usr_no, usr_name, usr_userlevel, usr_inst,
                usr_grade, usr_avatar, usr_document, usr_chat
        FROM users
        WHERE id = %s
    '''
    DR = db_result.DbResult(
        record_names,
        baseSelect(sql, (usr_id,))
    )
    return DR



def getAllProInfo(
        limit=None, page=None, state=0,
        initiatorId=None, sort=None, tagId=None
    ):
    record_names = (
        "id", "name", "sort", "releaseTime", "endTime", "need", "intro"
    )
    def initiatorApp(initiatorId=None):
        id_notNone = {
            "where": (' AND usr_pro.usr_id = %s '),
            "format": (initiatorId, )
        }
        id_None = {
            'where': (' '), "format": ()
        }
        return id_notNone if initiatorId is not None else id_None
    def sortApp(sort=None):
        sort_notNone = {
            "where": (' AND pro_sort = %s '),
            "format": (sort, )
        }
        sort_None = {
            'where': (' '), "format": ()
        }
        return sort_notNone if sort is not None else sort_None
    def tagApp(tagId=None):
        tag_notNone = {
            "join": (' LEFT JOIN pro_tag ON pro_tag.pro_id = projects.id ',),
            "where": (' AND pro_tag.tag_id = %s '),
            "format": (tagId, )
        }
        tag_None = {
            'join': ('  '),
            'where': ('  '),
            'format': ()
        }
        return tag_notNone if tagId is not None else tag_None
    def limitoff(limit=None, page=None):
        print(limit,page)
        if page is not None and limit is not None:
            lim_notNone = {
                'limoff': ' LIMIT %s OFFSET %s ',
                'format': (limit,(page - 1) * limit, )
            }
        else:
            lim_None = {
                'limoff': '  ',
                'format': ()
            }
        return lim_notNone if (limit is not None and page is not None) else lim_None
    def cat(tupleIn):
        __st = ""
        for elem in tupleIn:
            __st += elem
        return __st

    initiator = initiatorApp(initiatorId=initiatorId)
    sortor = sortApp(sort=sort)
    tagor = tagApp(tagId=tagId)
    limoff = limitoff(limit=limit, page=page)
    sql = '''
        SELECT id, pro_name, pro_sort, pro_releaseTime,
            pro_endTime, pro_need, pro_intro
        FROM projects
        LEFT JOIN usr_pro
        ON usr_pro.pro_id = projects.id
    ''' + cat(tagor['join']) + '''
        WHERE pro_deleted = 'N' AND pro_state = %s
    ''' + cat(initiator['where']) + cat(sortor['where']) + cat(tagor['where']) + '''
        AND usr_pro.upr_role = 'C'
        ORDER BY pro_releaseTime ''' + limoff['limoff']
    # TODO: should be attach importance that pro_state are supposed to be 1
    format_in = () + (state,) + initiator['format'] + sortor['format'] + tagor['format'] + limoff['format']
    print(format_in, sql)
    DR = db_result.DbResult(record_names, baseSelect(sql, format_in))
    return DR



def getAllCanBeShownCnt(table="projects"):
    record_name = ("total")
    if table == 'projects':
        # TODO: should be attach importance that pro_state are supposed to be 1
        sql = "SELECT COUNT(*) FROM " + table + " WHERE pro_deleted = 'N' AND pro_state = 0"
    DR = db_result.DbResult(
        record_name, baseSelect(sql, ())
    )
    return DR



def getProInfoById(id):
    record_names = ("name", "sort", "releaseTime", "endTime", "need", "intro")
    sql = '''
        SELECT pro_name, pro_sort, pro_releaseTime,
            pro_endTime, pro_need, pro_intro
        FROM projects
        WHERE id = %s
    '''
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (id,))
    )
    return DR



def getProInfoByInitiatorId(id, limit, page):
    sql = '''
        SELECT P.id, P.pro_name, P.pro_sort, P.pro_releaseTime,
            P.pro_endTime, P.pro_need, P.pro_intro
        FROM projects AS P
        LEFT JOIN usr_pro AS upr
        ON P.id = upr.pro_id
        WHERE upr.upr_role = 'C' AND upr.usr_id = %s AND NOW() < P.pro_endTime
        ORDER BY P.releaseTime
        LIMIT %s OFFSET %s
    '''
    record_name = (
        "id", "name", "sort", "releaseTime", "endTime", "need", "intro"
    )
    DR = db_result.DbResult(
        record_name, baseSelect(sql, (id, limit, (page - 1) * limit,))
    )
    return DR



# 用来在activity里面点出抽屉的时候，获取对应项目的request users
def getReqUsrInfoByProId(id):
    sql = '''
        SELECT U.id, U.usr_no, U.usr_name, U.usr_inst,
                U.usr_grade, U.usr_avatar, U.usr_document,
                rsp.rsp_time
        FROM users AS U
        LEFT JOIN response AS rsp
        ON U.id = rsp.usr_id
        LEFT JOIN projects AS P
        ON P.id = rsp.pro_id
        WHERE P.id = %s AND rsp.rsp_state = 'W' AND P.pro_deleted = 'N' AND P.pro_need > 0
        ORDER BY rsp.rsp_time DESC
    '''
    record_names = (
        "id", "no", "name", "inst",
        "grade", "avatar", "document", "rsp_time"
    )
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (id,))
    )
    return DR




def getProTagsByProId(id):
    record_names = ("tag_id", "tag_name")
    sql = '''
        SELECT id, tag_name FROM tags AS T
        LEFT JOIN pro_tag AS prt
        ON prt.tag_id = T.id
        WHERE prt.pro_id = %s
    '''
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (id,))
    )
    return DR


def getInitiatorInfoByProId(id):
    record_names = ("id", "no", "name", "inst", "avatar")
    sql = '''
        SELECT id, usr_no, usr_name, usr_inst, usr_avatar
        FROM users AS U
        LEFT JOIN usr_pro AS UP
        ON UP.usr_id = U.id
        WHERE UP.upr_role = 'C' AND UP.pro_id = %s
    '''
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (id,))
    )
    return DR



def getProOfATagId(id, limit, page):
    record_names = (
        "id", "name", "sort", "releaseTime", "endTime", "need", "intro"
    )
    sql = '''
        SELECT id, pro_name, pro_sort, pro_releaseTime,
            pro_endTime, pro_need, pro_intro
        FROM projects AS P
        LEFT JOIN pro_tag AS prt
        ON P.id = prt.pro_id
        WHERE prt.tag_id = %s AND pro_deleted = 'N' AND pro_state = 0
        ORDER BY pro_releaseTime
        LIMIT %s OFFSET %s
    '''
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (id,limit,(page - 1) * limit,))
    )
    return DR



def getTags():
    sql1 = '''
        SELECT id, tag_name FROM tags
    '''
    record_names1 = ("id", "name")
    DR = db_result.DbResult(
        record_names1, baseSelect(sql1, ())
    )
    return DR



def getRespondersInfoByProId(id):
    record_names = ("id", "no", "name", "inst", "avatar")
    sql = '''
        SELECT id, usr_no, usr_name, usr_inst, usr_avatar
        FROM users AS U
        LEFT JOIN usr_pro AS UP
        ON UP.usr_id = U.id
        WHERE UP.upr_role = 'F' AND UP.pro_id = %s
    '''
    DR = db_result.DbResult(
        record_names, baseSelect(sql, (id,))
    )
    return DR