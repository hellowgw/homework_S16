#!/usr/bin/env python
# coding:utf-8

location_dic = {'北京':
                    {
                        '朝阳':
                            {'安贞': ['信义大厦']},
                        '昌平':
                            {'沙河': ['oldboy', '阿泰包子']}
                    },
                '河北':
                    {
                        '石家庄':
                            {'北城区': ['河北移动大厦']},
                    }

                }
top_tag = 1
L1_tag = 1
L2_tag = 1
while top_tag:
    for i in location_dic:
            print(i)
    L1 = input('请选择省份(按q退出程序):  ')
    if L1 == 'q':
        break
    while L1_tag:
        for l in location_dic[L1]:
            print(l)
        L2 = input('请选择市/区(按b返回上一级菜单,按q退出程序):  ')
        if L2 == 'b':
            break
        if L2 == 'q':
            top_tag = 0
            break

        while L2_tag:
            for k in location_dic[L1][L2]:
                print(k)
            L3 = input('请选择区/街道(按b返回上一级菜单,按q退出程序):  ')
            if L3 == 'b':
                break
            if L3 == 'q':
                top_tag = 0
                L1_tag = 0
                break

            while True:
                for j in location_dic[L1][L2][L3]:
                    print(j)

                feet = input('按b返回上一级菜单,按q退出程序:  ')
                if feet == 'b':
                    break
                if feet == 'q':
                    top_tag = 0
                    L1_tag = 0
                    L2_tag = 0
                    break

print('程序退出')
