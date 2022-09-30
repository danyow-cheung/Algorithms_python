'''问题描述
数值转换，给定一个M进制的数x，实现对x向任意一个非M进制的数的转换
'''
'''问题分析
数制转换，需要了解一些概念
·基数：使用多少个不同的数字表示一个数值的大小，就称为该数制的基数，比如10进制为10
·权：x^2 x^4 x^6 x^10（maybe？）
'''
'''实现步骤
先定义两个函数实现字符与其对应数字之间的转换
'''

'''----------------------------tutorital version-------------------------------------'''
# 将字符转换成数字
def char_to_num(ch):
    if ch >= '0' and ch <= '9':
        return int(ch)  # 将数字字符转换成数字
    else:
        return ord(ch)  # 将字母字符转换成数字


# 将数字转换为字符
def num_to_char(num):
    if num >= 0 and num <= 9:
        return str(num)  # 将0~9之间的数字转换成字符
    else:
        return chr(num)  # 将大于10的数字转换成字符


# 其他数制转换为十进制
def source_to_decimal(temp, source):
    decimal_num = 0  # 存储展开之后的和

    for i in range(len(temp)):  # 累加
        decimal_num=(decimal_num * source)+char_to_num(temp[i])

    return decimal_num


# 十进制转换为其他数制
def decimal_to_object(decimal_num, object):
    decimal = []
    while decimal_num:
        decimal.append(num_to_char(decimal_num % object))# 求出余数并转换为字符
        decimal_num //= object  # 用十进制数除以基数

    return decimal


# 修改余数数制
def output(decimal):
    f = len(decimal)-1
    while f >= 0:
        print(decimal[f], end='')
        f -= 1
    print()

if __name__ == '__main__':
    MAXCHAR = 101  # 最大允许字符串长度
    flag = 1  # 存储是否退出程序的标志
    while flag:  # 利用输入的flag值控制循环是否结束
        print("转换前的数是：", end='')
        temp = input()
        print("转换前的数制是：", end='')
        source = int(input())
        print("转换后的数制是：", end='')
        object = int(input())
        print("转换后的数是：", end='')
        decimal_num = source_to_decimal(temp, source)
        decimal = decimal_to_object(decimal_num, object)
        output(decimal)
        print("继续请输入1,否则输入0：")
        flag = int(input())
'''----------------------------review version-------------------------------------'''


# 将字符转换为数字
def char_to_number(ch):
    if ch >= '0' and ch<='9':
        return int(ch)
    else:
        # ord()将字符转换为对应Unicode编码
        return ord(ch)
# 将数字转换为字符
def number_to_char(num):
    if num>= 0 and num<=9:
        return str(num)
    else:
        # ord()将十进制数字转换成对应的字符
        return chr(num)


'''其他数制转换为十进制，采用【按权展开相加】的方法，
需要定义一个变量来存储想加之后的和'''
# 其他进制转化为十进制
def source_to_decimal(temp,source):
    decimal_num = 0
    for i in range(len(temp)):
        decimal_num = (decimal_num*source)+char_to_number(temp[i])
    return decimal_num

# 十进制转化为其他进制
def decimal_to_source(demical_num,obj):
    demical = []
    while demical_num:
        # 求出余数并转换为字符
        demical.append(number_to_char(demical_num % obj))
        # 用十进制处以基数
        demical_num //= obj 
    return decimal

'''由余数组成的新数制数与余数顺序相反''' 
# 修改余数数制
def output(decimal):
    print(type(decimal))
    f = len(decimal) -1 
    while f>= 0:
        print(decimal[f],end="\n")
        f -= 1 
    print()


if __name__ =="__main__":
    maxchar = 101
    flag = 1 
    while flag:
        temp = input("plz enter \n")
        source = int(input("转换前的数制\n"))
        obj = int(input("转换后的数制\n"))
        decimal_num = source_to_decimal(temp,source)
        decimal = decimal_to_source(decimal_num,obj)
        output(decimal)
        print("继续输入1")
        flag = int(input())