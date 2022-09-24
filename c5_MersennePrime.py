'''問題描述【梅森素數】
梅森数(Mersenne Prime)指的是形如2^n-1的正整数，
其中 指数n是素数，记为Mn。如果一个梅森数是素数，则称其为梅森素数。
--试求出指数n<20的所有梅森素数。
'''
'''算法設計
设变量mp存储梅森数，整数i表示指数，其取值从2~19，
i每 变化一次，都相应地计算出一个梅森数，存放在mp中。

对每次计算 得到的当前mp值，都调用函数prime()进行判断。
'''
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
    n = 0 
    print("梅森素數")
    for i in range(2,20):
        mp = (2**i -1 )
        if prime(mp):
            n+=1 
            print(f"M({i})={mp}")
    print("2的指數n<20所有梅森素數有%d"%n)
            