#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def configsalt():
    file = open('config.json', encoding='utf-8')
    config = json.load(file)
    return config['auth'][0]['salt']


def configmysql():
    file = open('config.json', encoding='utf-8')
    config = json.load(file)
    mysql_config={'host':config['mysql'][0]['host'],'username':config['mysql'][0]['username'],'password':config['mysql'][0]['password']\
                  ,'database':config['mysql'][0]['database']}
    return mysql_config