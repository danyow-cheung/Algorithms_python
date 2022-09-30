'''問題描述【回文素數】
所谓回文素数指的是，
对一个整数n从左向右和从右向左读其数值都相同且n为素数，
则称整数n为回文素数。

求不超過1000的回文素數
'''
import math 

# 潘判斷素數
def fun(n):
    for i in range(2,(n-1)//2):
        if n% i ==0:
            return 0 
    return 1 

if __name__=='__main__':
    print("1000以内的回文素数:") 
    for i in range(0, 9+1):# 第一位
        for j in range(0,9+1):#第二位
            for k in range(0,9+1):#第三位
                n = i*100+j*10+k
                m = i+j*10+k*100
                # 處理整數的前兩位為0的情況
                if i==0 and j==0:
                    m = m//100
                #处理整数的第一位为0的情况
                elif i==0:
                    m = m//10 
                if n>10 and n==m and fun(n):
                    print("%d\t" %n, end="")
                
