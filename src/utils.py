#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
from authlib import config


# TODO:杂项：查询用户id,username,info,reg-date,last-date

def checkInfo(type,text,aim):
    return 0


def checkIdByUsername(username):
    mysql_config = config.configmysql()
    connection = pymysql.connect(mysql_config['host'], mysql_config['username'], mysql_config['password'],
                                 mysql_config['database'])
    cursor = connection.cursor()
    # 执行取最大id sql
    sql="SELECT `id` FROM quark.auth WHERE `username`='%s';" % \
                   (username)
    cursor.execute(sql)
    print(sql)
    sql_result = cursor.fetchall()
    # TODO:错误码统一
    for idrow in sql_result:
        if idrow[0] is None:
            return 2
        else:
            print(idrow)
            return idrow[0]


def checkUsernameById(id):
    return 0


def checkInfoById(id):
    return 0


def checkInfoByUsername(username):
    return 0


def checkDateByUsername(username):
    return 0


def checkDateById(id):
    return 0
