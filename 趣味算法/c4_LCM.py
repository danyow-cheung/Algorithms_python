'''問題描述【最小公倍數】
求任意两个正整数的最小公倍数(Least Common Multiple， LCM)。
'''


'''問題分析
计算最小公倍数时，通常会借助最大公约数来辅助计算，
即最小公倍数=两数的乘积/最大公约(因)数，'''

'''算法分析
两个整数的最小公倍数不小于两数中的任意一个，
-如果大数不是小数的倍数，则由大数开始利用递增方法找到第一个满足条件的数
'''
if __name__ =='__main__':
    m = int(input("请输入整数m = "))
    n = int(input("请输入整数n = "))

    if m<n:
        temp = m 
        m = n 
        n = temp 
    
    i =  m 
    # 从大数开始寻找满足条件的自然数
    while i> 0:
        if i%m == 0 and i% n == 0:
            print("%d 和 %d 的最小公倍数为:%d" %(m, n, i))
            break
        i+= 1
    
'''# 最小公倍数——利用两数的最大公约数求出最小公倍数'''
# if __name__ == "__main__":
#     m = int(input("请输入整数m = "))
#     n = int(input("请输入整数n = "))
#     # k存储两数的乘积
#     k = m*n
#     print("%d 和 %d 的最小公倍数为" %(m, n))

#     if m<n:
#         temp = m 
#         m = n 
#         n = temp 
#     # b存储m除以n的余数
#     b = m%n 

#     while b!=0:
#         # 原来的小数作为下次运算的大叔
#         m = n
#         # 将上一次的余数作为下次相除时的小数
#         n = b 
        
#         b = m%n 
#     # 两数相乘除以最大公约数即位他们最小的公倍数
#     resultNum = k//n 
#     print("%d"%resultNum)