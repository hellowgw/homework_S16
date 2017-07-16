#!/usr/bin/env python
# coding:utf-8
product_list = [
                   {1: {'ipad': 2899}},
                   {2: {'switch': 2499}},
                   {3: {'bike': 1500}},
                   {4: {'coffee': 32}},
                ]

cart_dic = {}
buy_price_dic = {}
current = int(input('请输入工资收入:  '))
while True:
    print('\n############# 价目表 #############')
    for d in product_list:
        for pro_id in d:
            for pro_name in d[pro_id]:
                print('%s   %s   $%s' % (pro_id, pro_name, d[pro_id][pro_name]))

    choice = input('请输入商品编号(按q退出):  ')
    if choice == 'q':
        if cart_dic:
            print('名称   个数   单价   总价')
            for buy_name in cart_dic:
                for (buy_price, buy_count) in cart_dic[buy_name].items():
                    print('%s   %s   %s   %s' %(buy_name, buy_count, buy_price, int(buy_count)*int(buy_price)))
        print('\n欢迎再次光临')
        break

    else:
        choice_id = int(choice)
        list_index = choice_id - 1
        pro_info = product_list[list_index][choice_id]
        for (k, v) in pro_info.items():
            choice_name = k
            choice_price = int(v)
            if choice_price > current:
                    print('\n对不起,您的余额不足\n')
            else:
                current = current - choice_price
                if cart_dic.__contains__(choice_name):
                    cart_dic[choice_name][choice_price] += 1

                else:
                    buy_price_dic = {}
                    buy_price_dic[int(choice_price)] = 1
                    cart_dic[choice_name] = buy_price_dic


    print('您当前的余额是 %s 元 \n' % current)









