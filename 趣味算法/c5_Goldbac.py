'''問題描述【哥德巴赫猜想】
2000以內的不小於4的正偶數能夠分解兩個素數之和
'''
'''問題分析
驗證成立首先要把整數分解為兩部分，然後判斷分解出的兩個整數是否均為素數
'''

'''算法設計
【1】fun(n)函數判斷輸入的n值是否為素數
    -n=2，是素數返回1
    -n是偶數，不是素數，返回0
    -n是奇數，不是素數，返回0
    -n!=2 是素數，返回1
【2】guess(n)函數用於驗證哥德巴赫猜想
'''
import math 
# 判斷是否為素數
def fun(n):
    # n是2，返回1
    if n==2:
        return 1 
    # n是偶數，不是素數，返回0
    if n%2 ==0:
        return 0 
    
    i= 3 
    # n是奇數，不是素數，返回0
    while i<= math.sqrt(n):
        if n%i ==0:
            return 0 
        i+=2 
    return 1 
# n是除2以外的素數，返回1

# 驗證哥德巴赫猜想
def guess(n):
    # 進入循環前先設置標誌位
    ok = 0 
    i = 2 
    while i<=(n//2):
        if fun(i):
            if fun(i-1):
                # i和i-1都是素數，則打印
                print("%d  %d\n" % (i, n - i))
                ok = 1 
        if i!= 2:
            i+= 1
        if ok:
            break
        i+=1 

if __name__ =="__main__":
    while True:
        n = int(input("輸入"))
        guess(n)