#!/usr/bin/env python
# coding:utf-8

file = 'staff.txt'
file_tmp = 'staff.tmp'


def check_file(filename):
    """检测是否有这个文件,文件不存在就创建一个空文件"""
    import os
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass
    else:
        with open(filename, 'r+') as f:
            """文件存在就读取内容,如果删除回车和空格之后还有其他
            就什么都不做,如果删除回车和空格之后就什么都没有了,就把
            文件指针调整到文件最开始的位置,并清空成为一个空文件"""
            for i in f.readlines():
                if i.strip():
                    pass
                else:
                    f.seek(0)
                    f.truncate()


def add_user(info_dict):
    """把字典的内容读出来,按指定顺序写入列表,拼接成字符串后存入文件"""
    info_list = []
    check_file(file)
    with open('staff.txt', 'r+') as f:
        """读取当前文件内已经存在的行数,+1之后做为新一行的行号"""
        uid = str(len(f.readlines())+1)
        info_list.append(uid)
        info_list.append(info_dict['user'])
        info_list.append(info_dict['age'])
        info_list.append(info_dict['phone'])
        info_list.append(info_dict['job'])
        info_list.append(info_dict['date'])
        info_str = ','.join(info_list)
        f.write(info_str)
        f.write('\n')


def select(method, keyword):
    line_list = []
    with open(file) as f:
        for i in f:
            info_list = i.strip().split(',')
            uid = info_list[0]
            age = int(info_list[2])
            job = info_list[4]
            date = info_list[5]
            if method == 'ge' and age > keyword:
                print(age)
                line_list.append((int(uid)-1))
            if method == 'eq' and job == keyword:
                line_list.append(uid)
            if method == 'like' and keyword in date:
                    line_list.append(uid)
        f.seek(0)
        for x in line_list:
            f.seek(0)
            print(f.readlines()[int(x)])


def del_user(user_id):
    """根据输入的用户id删除对应的记录.遍历数据文件
    将不包含用户id的行写入到临时文件中.最后清空原始
    数据文件,将临时文件中的内容写回到数据文件中"""
    with open(file, 'r+') as f:
        with open(file_tmp, 'w+') as f_tmp:
            for i in f:
                uid = int(i.strip().split(',')[0])
                if user_id != uid:
                    f_tmp.write(i)
            # 调整临时文件的指针到文件顶部
            f_tmp.seek(0)
            # 清空数据文件的内容
            f.seek(0)
            f.truncate()
            # 遍历临时文件将内容写入数据文件
            for x in f_tmp:
                f.write(x)


def update_user(job_src, job_dst):
    """更新用户职业信息.找对对应的列,修改列表对应的索引的值.
    然后将所有的内容写入临时文件,再最后写入数据文件中"""
    with open(file, 'r+') as f:
        with open(file_tmp, 'w+') as f_tmp:
            for i in f:
                job = i.strip().split(',')
                if job[4] == job_src:
                    job[4] = job_dst
                info_str = ','.join(job)
                f_tmp.write(info_str)
                f_tmp.write('\n')
            f_tmp.seek(0)
            f.seek(0)
            f.truncate()
            for x in f_tmp:
                f.write(x)



my_dict = {
    'user': 'wgw',
    'age': '33',
    'phone': '138811554646',
    'job': 'it',
    'date': '2013-04-01'
}
my_dict2 = {
    'user': 'alex',
    'age': '18',
    'phone': '138811553123',
    'job': 'market',
    'date': '2011-02-01'
}

"""
基本功能已经实现,没有做异常处理.没有做phone值唯一的认证
"""
del_user(5)
add_user(my_dict)
select('ge', 10)
update_user('it', 'aaa')
