#!/usr/bin/env python
# coding:utf-8
import logging
import os
from api.mapi.manage_api import check_file

base_dir = os.path.dirname(os.path.dirname(__file__))
log_path = '{0}/data'.format(base_dir)


# def save_log(user, msg):
#     file = '{0}/{1}.log'.format(log_path, user)
#     logging.basicConfig(level=logging.INFO,
#                 format='%(asctime)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename=file,
#                 filemode='a')
#     check_file(file)
#     logging.info(msg)

def save_log(user, msg):
    file = '{0}/{1}.log'.format(log_path, user)
    check_file(file)
    with open(file, 'a') as f:
        f.write(msg)
