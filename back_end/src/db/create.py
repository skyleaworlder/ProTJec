from .. import db_result
import pymysql
from . import baseSelect

def userInfoInsert(
        usr_no, usr_password, usr_name,
        usr_userlevel, usr_inst, usr_grade, usr_avatar
    ):
    sql1 = '''
        INSERT INTO users(
            usr_no, usr_password, usr_name,
            usr_userlevel, usr_inst, usr_grade, usr_avatar
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s
        )
    '''
    sql2 = '''
        SELECT id, usr_no FROM users
        WHERE usr_no = %s
    '''

    baseSelect(sql1, (
        usr_no, usr_password, usr_name,
        usr_userlevel, usr_inst, usr_grade, usr_avatar,
    ))
    record_names = ("id", "no")
    DR = db_result.DbResult(
        record_names, baseSelect(
            sql2, (usr_no,)
        )
    )
    return DR



def proAdd(
        usr_id, pro_name, pro_sort, pro_releaseTime,
        pro_endTime, pro_need, pro_intro
    ):
    record_name = ('id',)
    sql0 = '''
        INSERT INTO projects(
            pro_name, pro_sort, pro_releaseTime,
            pro_endTime, pro_need, pro_intro
        ) VALUES (
            %s, %s, %s,
            %s, %s, %s
        )
    '''
    sql1 = '''
        SELECT id FROM projects
        WHERE pro_name = %s AND pro_releaseTime = %s
    '''
    sql2 = '''
        INSERT INTO usr_pro (
            usr_id, pro_id
        ) VALUES (
            %s, %s
        )
    '''
    sql3 = '''
        SELECT P.id, UP.upr_role
        FROM projects AS P
        LEFT JOIN usr_pro AS UP
        ON P.id = UP.pro_id
        WHERE P.pro_name = %s AND P.pro_releaseTime = %s AND UP.upr_role = 'C'
    '''
    # first, insert pro info
    baseSelect(sql0, (
        pro_name, pro_sort, pro_releaseTime,
        pro_endTime, pro_need, pro_intro
    ))
    # second, get pro id
    pro_id = db_result.DbResult(
        record_name, 
        baseSelect(
            sql1, (pro_name, pro_releaseTime,)
        )
    ).records()[0]['id']
    # third, use pro and usr id to insert upr
    baseSelect(sql2, (usr_id, pro_id,))
    # last, get check
    record_names = ("id", "role")
    DR = db_result.DbResult(
        record_names, baseSelect(
            sql3, (pro_name, pro_releaseTime,)
        )
    )
    return DR



def attemptJoin(rsp_time, rsp_state, usr_id, pro_id):
    sql1 = '''
        INSERT INTO response (
            rsp_time, rsp_state, usr_id, pro_id
        ) VALUES (
            %s, %s, %s, %s
        )
    '''
    sql2 = '''
        SELECT usr_id, pro_id
        FROM response
        WHERE rsp_state = 'W' AND rsp_time = %s
    '''
    baseSelect(sql1, (rsp_time, rsp_state, usr_id, pro_id,))
    record_names = ("usr_id", "pro_id")
    DR = db_result.DbResult(
        record_names, baseSelect(sql2, (rsp_time,))
    )
    return DR


def capAgreeJoin(
        usr_id, pro_id
    ):
    sql1 = '''
        INSERT INTO usr_pro (
            upr_role, usr_id, pro_id
        ) VALUES (
            'F', %s, %s
        )
    '''
    sql2 = '''
        SELECT upr_role, usr_id, pro_id
        FROM usr_pro
        WHERE upr_role = 'F' AND usr_id = %s AND pro_id = %s
    '''
    baseSelect(sql1, (usr_id, pro_id))
    record_names = ('role', 'usr_id', 'pro_id')
    DR = db_result.DbResult(
        record_names, baseSelect(sql2, (usr_id, pro_id,))
    )
    return DR



def addTagsOfPro(pro_id, tag_id):
    sql1 = '''
        INSERT INTO pro_tag (
            pro_id, tag_id
        ) VALUES (
            %s, %s
        )
    '''
    sql2 = '''
        SELECT pro_id, tag_id
        FROM pro_tag
        WHERE pro_id = %s AND tag_id = %s
    '''
    baseSelect(sql1, (pro_id, tag_id,))
    record_names = ('pro_id', 'tag_id')
    DR = db_result.DbResult(
        record_names, baseSelect(sql2, (pro_id, tag_id,))
    )
    return DR