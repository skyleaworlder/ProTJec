from .. import db_result
import pymysql
from . import baseSelect


def delById(id, table='projects'):
    sql1 = "DELETE FROM " + table + " WHERE id = " + id
    sql2 = "SELECT id FROM " + table + " WHERE id = " + id
    baseSelect(sql1, (id,))
    record_name = ("id")
    DR = db_result.DbResult(
        record_name, baseSelect(sql2, (id,))
    )
    return DR