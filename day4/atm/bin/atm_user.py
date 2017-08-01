#!/usr/bin/env python
# coding:utf-8
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from api.uapi.userapi import *
from core.auth_user import auth


@auth
def start_run(user, serv_dic):
    for i in range(1, len(serv_dic)+1):
        print(i, serv_dic[i])
    service_id = int(input('请选择您要办理的业务:  '))
    if service_id == 1:
        money = int(input('请输入要存入的金额:  '))
        result = repayment(user, money)
        print(result)
    elif service_id == 2:
        money = int(input('请输入要取出的金额:  '))
        result = takemoney(user, money)
        print(result)
    elif service_id == 3:
        to_user = input('请输入对方的账号:  ')
        money = int(input('请输入要转账的金额:  '))
        result = transfer(user, to_user, money)
        print(result)
    elif service_id == 4:
        print('print log')
    else:
        print('没有这个选项')

if __name__ == '__main__':
    service_dic = {
        1: '存钱',
        2: '取钱',
        3: '转账',
        4: '打印账单'
    }
    username = input('请输入用户名: ')
    start_run(username, service_dic)
