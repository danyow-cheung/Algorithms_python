'''問題描述【要發就發】
请将不超过1993的所有素数从小到大 排成第一行，
第二行上的每个数都等于它上面相邻两个素数之差。 
编程求出:第二行数中是否存在若干个连续的整数，
它们的和恰好 为1898?假如存在的话，又有几种这样的情况
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


if __name__ =='__main__':
    count = 0
    print("列出第一行中差值为1898的所有素数组合: ")
    j = 0 
    i = 3 
    number = [0]*320 
    while i <= 1993:
        if fun(i):
            j = j+1  
            number[j] = i
        i+=2 
    j = j -1 
    # 最大的素數向1898探索
    while number[j]>1898:
        # 循環查找滿足條件的素數
        i = 0 
        while number[j] - number[i]>1898:
            i+=1 
        # 若兩個素數的差為1898，則輸出
        if number[j] - number[i]==1898:
            count += 1
            print("(%d). %3d,  %d" %(count,number[i], number[j]))        
        j-= 1

    