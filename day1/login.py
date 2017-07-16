#!/usr/bin/env python
# -*- coding:utf-8 -*-
login_count = 0
while True:
    login_count += 1
    user = input('username: ')
    pwd = input('password: ')
    if login_count > 3:
        print('您已被锁定！！！')
    else:
        if user == 'wgw' and pwd == '123':
            break
        else:
            print('错误的用户名或密码')
            print('已经尝试登录 %s 次' % login_count)

print('欢迎光临')
