import pymysql
import traceback
from .. import db_result


__connect_auth = ("localhost","Serendipity","Ljg19990426!","ProTJec")


def baseSelect(sqlInput, tupleInput):
    db = pymysql.connect(*__connect_auth)
    cursor = db.cursor()

    try :
        cursor.execute(sqlInput, tupleInput) # 避免SQL注入攻击
        db.commit()
        returnValue = cursor.fetchall()
    except Exception:
        db.rollback()
        traceback.print_exc()
        return
    finally :
        db.close()

    return returnValue
