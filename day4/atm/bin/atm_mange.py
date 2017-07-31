#!/usr/bin/env python
# coding:utf-8
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from api.mapi.manage_api import *


def start_backend(service_dic):
    for i in range(1, len(service_dic)+1):
        print(i, service_dic[i])
    service_id = int(input('请选择您要办理的业务：  '))
    if service_id == 1:
        user = input('输入用户名:  ')
        pwd = input('输入密码:  ')
        quota = int(input('输入用户额度: '))
        user_dic = {user: [pwd, quota, 0]}
        result = add_user(user_dic)
        print(result)
    elif service_id == 2:
        user = input('输入用户名:  ')
        quota = int(input('输入用户额度: '))
        result = modify_quota(user, quota)
        print(result)
    elif service_id == 3:
        user = input('输入用户名:  ')
        result = lock_user(user)
        print(result)
    else:
        print('没有这个选项')

if __name__ == '__main__' :
    service_dic = {
        1: '添加用户',
        2: '修改用户额度',
        3: '锁定用户'
    }
    start_backend(service_dic)