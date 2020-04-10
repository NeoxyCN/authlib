#!/usr/bin/env python
# -*- coding: utf-8 -*-
from authlib import config
import pymysql
import time
import datetime


# TODO:封禁部分

def ban(username, reason, bantime, bannerid):
    # status=2
    result = 0
    bandate = int(
        time.mktime(time.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')))
    unbandate = int(time.mktime(
        time.strptime((datetime.datetime.now() + datetime.timedelta(hours=bantime)).strftime('%Y-%m-%d %H:%M:%S'),
                      '%Y-%m-%d %H:%M:%S')))
    # 声明mysql连接参数并创建连接
    mysql_config = config.configmysql()
    connection = pymysql.connect(mysql_config['host'], mysql_config['username'], mysql_config['password'],
                                 mysql_config['database'])
    cursor = connection.cursor()
    # 执行取最大id sql
    cursor.execute('SELECT MAX(banid) AS max_id FROM quark.`auth-ban`;')
    sql_result = cursor.fetchall()
    for maxid_row in sql_result:
        if maxid_row[0] is None:
            maxbanid = 1
        else:
            maxbanid = int(maxid_row[0]) + 1
    # 先对auth表操作 status banid
    # TODO:此处应当进行id和username双认证
    sql = "UPDATE quark.auth SET status='2',banid='%s' WHERE username='%s';" % \
          (maxbanid, username)
    # TODO:统一错误码
    try:
        cursor.execute(sql)
        connection.commit()
    except:
        result = 2
    # 再对auth-ban表操作 banid
    sql = "INSERT INTO quark.`auth-ban` (banid,username,`ban-date`,`unban-date`,`ban-reason`,`bannerid`) " \
          "VALUES ('%s','%s','%s','%s','%s','%s');" % \
          (maxbanid, username, bandate, unbandate, reason, bannerid)
    try:
        cursor.execute(sql)
        connection.commit()
    except:
        result = 2
    # 关闭连接
    connection.close()
    return result


def unban(username):
    return 0


def delet(username):
    return 0


def checkUnbanDateByUsername(username):
    return 0


def checkUnbanDateById(id):
    return 0


def checkBanReasonByUsername(username):
    return 0


def checkBanReasonById(id):
    return 0
