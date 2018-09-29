import pymysql
from flask_settings import CONFIG

def py_mysql(sql,args):
    conn = pymysql.connect(**CONFIG)
    cursor = conn.cursor()
    user = cursor.execute(sql,args)
    conn.commit()
    conn.close()
    return user
def py_mysql_all(sql,*args):
    conn = pymysql.connect(**CONFIG)
    cursor = conn.cursor()
    cursor.execute(sql,*args)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def py_mysql_one(sql,*args):
    conn = pymysql.connect(**CONFIG)
    cursor = conn.cursor()
    cursor.execute(sql,*args)
    results = cursor.fetchone()
    conn.commit()
    conn.close()
    return results