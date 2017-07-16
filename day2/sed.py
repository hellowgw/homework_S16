#!/usr/bin/env python
# coding:utf-8
import sys
import os
old_str = sys.argv[1]
new_str = sys.argv[2]
file_name = sys.argv[3]
tmp_file = '%s_tmp' % file_name

with open(tmp_file, 'w+') as f_new:
    with open(file_name, 'r') as f:
        for i in f:
            data = i.replace(old_str, new_str)
            f_new.write(data)

os.remove(file_name)
os.rename(tmp_file, file_name)

