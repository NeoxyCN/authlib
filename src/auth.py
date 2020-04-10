#!/usr/bin/env python
# -*- coding: utf-8 -*-
from authlib import config
import time
import uuid
import hashlib
import pymysql


# TODO:登陆部分
def login(username, password):
    return 0


def register(username, password):
    result = 0
    # TODO:密码验证 只能是英文数字标点符号
    # TODO:查重用户名 只能有一个
    # 声明mysql连接参数并创建连接
    mysql_config = config.configmysql()
    connection = pymysql.connect(mysql_config['host'], mysql_config['username'], mysql_config['password'],
                                 mysql_config['database'])
    # 获取cursor
    cursor = connection.cursor()
    # 执行取最大id sql
    cursor.execute('SELECT MAX(id) AS max_id FROM quark.auth;')
    sql_result = cursor.fetchall()
    for maxid_row in sql_result:
        if maxid_row[0] is None:
            maxid = 0
        else:
            maxid = int(maxid_row[0]) + 1
    # 循环取出数组中最大值
    # 取注册时间戳
    register_time = int(time.time())
    # 取用户名uuid
    register_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, username)
    # 取盐
    salt = config.configsalt()
    # password加盐取SHA256
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf8') + salt.encode('utf8'))
    # 创建用户的sql
    sql = "INSERT INTO quark.auth " \
          "(id,uuid,status,banid,`exp`,`group`,username,password,money,info,ip,`reg-date`,`last-date`) " \
          "VALUES ('%s','%s','0','0','0','1','%s','%s','0','0','0','%s','%s');" % \
          (maxid, register_uuid, username, sha256.hexdigest(), register_time, register_time)
    # 尝试执行 不行就会滚 出错返回1 没事返回0
    # 不过为什么上面的取最大id不try呢 qwq
    # TODO:统一错误码
    try:
        cursor.execute(sql)
        connection.commit()
    except:
        # 不是很懂这里pycharm报的 Too broad exception clause
        result = 2
    # 关闭连接
    connection.close()
    return result
