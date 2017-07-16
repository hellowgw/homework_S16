#!/usr/bin/env python
# coding:utf-8
import os
import json
file = 'user.txt'
app_path = os.path.abspath('..')
data_path = '%s/data' % app_path
os.chdir(data_path)


def check_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass


def write_info(info_dic):
    json_dic = json.dumps(info_dic)
    with open(file, 'w') as f:
        f.write(json_dic)


def read_info():
    check_file(file)
    with open(file, 'r') as f:
        content = f.read()
        if content:
            user_dic = json.loads(content)
        else:
            user_dic = {}
        return user_dic


def add_user(user_dic):
    info_dic = read_info()
    for i in user_dic:
        if i not in info_dic:
            info_dic[i] = user_dic[i]
            write_info(info_dic)
            ret = '新用户 %s 创建成功' % i
        else:
            ret = '用户 %s 已经存在' %i
        return ret


def modify_quota(username, quota_number):
    info_dic = read_info()
    if username in info_dic:
        info_dic[username][1] = quota_number
        write_info(info_dic)
        ret = '已将用户 %s 的余额修改为 %s 元' % (username, quota_number)
    else:
        ret = '没有找到用户 %s 的账号信息' % username
    return ret

def lock_user(username):
    pass

a = {
    'wgw': ['wgw123', 15000, '0']
}

#print(adduser(a))
print(modify_quota('wgw', 30000))
