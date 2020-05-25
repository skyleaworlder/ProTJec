from .. import db_result
import pymysql
from . import baseSelect


def proNeedDecrease(pro_id):
    sql1 = '''
        UPDATE projects AS P
        SET P.pro_need = P.pro_need - 1
        WHERE P.id = %s AND P.pro_need > 0
    '''
    sql2 = '''
        SELECT P.id, P.pro_need
        FROM projects AS P
        WHERE P.id = %s
    '''
    record_names = ('id', 'need')
    baseSelect(sql1, (pro_id,))
    DR = db_result.DbResult(
        record_names,
        baseSelect(sql2, (pro_id,))
    )
    return DR


def changeProState(pro_id, state):
    sql1 = '''
        UPDATE projects AS P
        SET P.pro_state = %s
        WHERE P.id = %s
    '''
    sql2 = '''
        SELECT P.id, P.pro_state
        FROM projects AS P
        WHERE P.id = %s
    '''
    record_names = ('id', 'state')
    baseSelect(sql1, (state, pro_id))
    DR = db_result.DbResult(
        record_names,
        baseSelect(sql2, (pro_id,))
    )
    return DR



def changeRspState(usr_id, pro_id, state):
    sql1 = '''
        UPDATE response AS rsp
        SET rsp.rsp_state = %s
        WHERE rsp.usr_id = %s AND rsp.pro_id = %s
    '''
    sql2 = '''
        SELECT rsp.rsp_time, rsp.rsp_state,
            rsp.usr_id, rsp.pro_id
        FROM response AS rsp
        WHERE rsp.usr_id = %s AND rsp.pro_id = %s AND rsp.rsp_state = %s
    '''
    record_names = ('time', 'state', 'usr_id', 'pro_id')
    baseSelect(sql1, (state, usr_id, pro_id))
    DR = db_result.DbResult(
        record_names, baseSelect(sql2, (usr_id, pro_id, state))
    )
    return DR


def changeUsrInfo(
        id, usr_name, usr_no, usr_inst,
        usr_grade, usr_document, usr_chat, usr_avatar
    ):
    sql1 = '''
        UPDATE users AS U
        SET U.usr_name = %s, U.usr_no = %s, U.usr_inst = %s, U.usr_grade = %s,
            U.usr_document = %s, U.usr_chat = %s, U.usr_avatar = %s
        WHERE U.id = %s
    '''
    sql2 = '''
        SELECT usr_no, usr_name, usr_inst, usr_grade,
            usr_document, usr_chat, usr_avatar
        FROM users
        WHERE id = %s
    '''
    baseSelect(sql1, (
        usr_name, usr_no, usr_inst, usr_grade,
        usr_document, usr_chat, usr_avatar, id,
    ))
    record_names = ("no", "name", "inst", "grade", "document", "chat", "avatar")
    DR = db_result.DbResult(
        record_names, baseSelect(sql2, (id,))
    )
    return DR



def updateProInfo(
        id, pro_name, pro_sort,
        pro_intro, pro_need
    ):
    sql1 = '''
        UPDATE projects AS P
        SET P.pro_name = %s, P.pro_sort = %s,
            P.pro_intro = %s, P.pro_need = %s
        WHERE P.id = %s
    '''
    sql2 = '''
        SELECT id FROM projects
        WHERE id = %s AND pro_name = %s AND pro_sort = %s
    '''
    baseSelect(sql1, (
        pro_name, pro_sort, pro_intro, pro_need, id,
    ))
    record_names = ("id")
    DR = db_result.DbResult(
        record_names, baseSelect(sql2, (id, pro_name, pro_sort,))
    )
    return DR