#!/usr/bin/env python
# coding:utf-8
from ..mapi.manage_api import (read_info, write_info)

info_dic = read_info()


def repayment(username, repay_number):
    if username in info_dic:
        info_dic[username][1] = info_dic[username][1] + repay_number
        write_info(info_dic)
        ret = '用户 {0} 还款 {1}元 成功'.format(username, repay_number)
    else:
        ret = '用户 {0} 不存在!!'.format(username)
    return ret


def takemoney(username, money_number):
    if username in info_dic:
        tips = money_number*0.05
        if info_dic[username][1] - money_number - tips >= 0:
            info_dic[username][1] = info_dic[username][1] - money_number - tips
            write_info(info_dic)
            ret = '用户 {0} 成功提取现金: {1}元 手续费:{2}元'.format(username, money_number, tips)
        else:
            ret = '用户 {0} 余额不足'
    else:
        ret = '用户 {0} 不存在!!'.format(username)
    return ret


def transfer(src_name, dst_name, transfer_number):
    if src_name in info_dic:
        if dst_name in info_dic:
            if info_dic[src_name][1] - transfer_number >= 0:
                info_dic[src_name][1] = info_dic[src_name][1] - transfer_number
                print(info_dic[src_name][1])
                info_dic[dst_name][1] = info_dic[dst_name][1] + transfer_number
                print(info_dic)
                write_info(info_dic)
                ret = '用户 {0} 成功转账给用户 {1} {2}元'.format(src_name, dst_name, transfer_number)
            else:
                ret = '用户 {0} 余额不足'.format(src_name)
        else:
            ret = '用户 {0} 不存在!!'.format(dst_name)
    else:
        ret = '用户 {0} 不存在!!'.format(src_name)
    return ret
