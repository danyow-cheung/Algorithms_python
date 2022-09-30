'''問題描述【素數】
素数是指除了1和它本身以外再没有其他因子的自然数。
在所有的素数中，
只有2是唯一的一个偶数，其他的素数都是奇数。
'''
'''算法設計
外層循環對每個數進行迭代，逐一檢查是否為素數
'''

''' 求素數'''
# 外層循環，對start-end之間的每個數進行迭代，檢查是否為素數
from itertools import count
import math 

# m = start 
# while m <= end:
#     # 求m的平方根
#     k = math.sqrt(m)
#     i = 2 
#     # 內層循環，判斷2～k之間的每個數是否能被m整除
#     while i<=k:
#         # 若存在一個數能被m整除,則跳出內層循環
#         # 若則，m是素數打印m
#         i+= 1
#     m+= 1

if __name__ =='__main__':
    flag= 1
    count = 0 
    start = int(input("請輸入start = "))
    end = int(input("請輸入end = "))
    if start<1 or end < start:
        print("輸入又誤")
        exit(0)
    m = start 
    print("%d 和 %d 之间的素数有:" %(start, end))
    while m<= end:
        # 求m的平方根
        k = math.sqrt(m)
        i = 2 
        # 內層循環，判斷2~k之間的每個數是否能被m整除
        while i<= k:
            # 若存在一個數能被m整除，則跳出內層循環
            if m%i ==0:
                flag = 0
                break 
            i+= 1
        #如果flag==1，則當前的數位素數 
        if flag==1:
            print("%-4d"%m,end="")
            count+= 1
        flag = 1 
        m+= 1
    print("\n%d 到 %d之间共有:%d 个素数" %(start, end, count))

'''問題擴展
求素數的優化算法
'''
k = int(math.sqrt(m))
for i in range(2,k+2):
    if m% i==0:
        break
if i==k +1:
    print(m, "是素数!")
else:
    print(m, "不是素数!")