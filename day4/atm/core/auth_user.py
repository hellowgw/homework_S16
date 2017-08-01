#!/usr/bin/env python
# coding:utf-8
from api.mapi.manage_api import read_info


def auth(func):
    def wrapper(user, serv_dic):
        pwd = input('请输入密码:  ')
        user_info = read_info()
        if user in user_info:
            if user_info[user][0] == pwd:
                print('欢迎光临')
                ret = func(user, serv_dic)
                return ret
    return wrapper
