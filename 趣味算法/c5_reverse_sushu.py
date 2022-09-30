'''問題描述【可逆素數】
輸出所有4位數的可逆素數

'''
import math 

# 潘判斷素數
def fun(i):
    # n<=1顯然不是素數
    if i<=1:
        return 0 
    if i==2:
        return 1 
    # 是偶數，不是素數
    if i%2==0:
        return 0
    for j in range(3,int(math.sqrt(i)+1)):
        # n是奇數，不是素數返回0
        if i%j==0:
            return 0 
        j+=2 
        # n是除2以外的素數，返回1
    return 1 

if __name__ =="__main__":
    # 計數器
    count = 0

    # 窮舉法
    for a in range(1,9+1):#千位
        for b in range(0,9+1):# 百位
            for c in range(0,9+1):# 十位
                for d in range(1,9+1):#個位
                    if fun(a*1000+b*100+c*10+d):        
                        if fun(a+b*10+c*100+d*1000):
                            if count % 10 == 0: # 每10个数就换行 
                                print()
                            print("%d   " %(a*1000+b*100+c*10+d), end="")
                            count += 1

    print("\n4位可逆素数共有%d个" %count)
