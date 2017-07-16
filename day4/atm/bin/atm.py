#!/usr/bin/env python
# coding:utf-8


def start_run(service_dic):
    for i in range(1, len(service_dic)+1):
        print(i, service_dic[i])
    service_id = int(input('请选择您要办理的业务：  '))
    if service_id == 1:
        print('save money')
    elif service_id == 2:
        print('take money')
    elif service_id == 3:
        print('transfer money')
    elif service_id == 4:
        print('print log')
    else:
        print('没有这个选项')

if __name__ == '__main__' :
    service_dic = {
        1: '存钱',
        2: '取钱',
        3: '转账',
        4: '打印账单'
    }
    start_run(service_dic)
