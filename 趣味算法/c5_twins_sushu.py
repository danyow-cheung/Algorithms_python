'''問題描述【孿生素數】
所谓孪生素数指的是间隔为2的两个相邻素数，
因为它们之间的距离已经近得不能再近了，如同孪生姊妹一样，
故将这一对素数称 为孪生素数
---编程求出3~1000以内的所有孪生素数。
'''

import math 

# 潘判斷素數
def fun(n):
    k = math.sqrt(n)+1
    i =2 
    while i<=k:
        if n%i ==0:
            return 0 
        i+=1 
    return 1 

import math
# 判断n是否为素数 
def prime(n):
    k = math.sqrt(n) + 1 
    i= 2
    while i <= k:
        if n % i == 0:
            return 0
        i+=1 

    return 1 

if __name__=='__main__':
    count = 0 
    print("3到1000之间的孪生素数:") 
    for i in range(3, 1000):
        if prime(i) and prime(i+2):
            print("(%-3d, %3d)  " %(i, i+2), end="")
            count += 1
            if count % 5 == 0:
                print() 
    print("\n1000以内的孪生素数共有%d对" %count)

