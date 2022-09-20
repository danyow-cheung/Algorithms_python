'''問題描述【親密數】
如果整數A的全部因子（包括1，不包括本身）之和等於B，
且B的全部因子（包括1，不包括本身）之和等於A，
則稱A和B是親密數，求3000內全部的親密數
'''

'''問題分析
要判斷整數a是否有親密數，先計算出a的全部因子的累加和，將其存到變量b，
再計算b的全部因子的累加和設為n，若a=n則為親密數'''


'''算法分析
计算数a的各因子的算法：
用a依次对i（i的范围可以是1～a-1或1～a/2-1）
进行模（“%”，在编程过程中一定要注意求模符号两边参加运算的数据必须为整数）运算，
若结果等于0，则i为a的一个因子；否则i就不是a的因子。将所求得的因子累加到变量b。

求變量B的因子算法也相同
'''

# 窮舉3000以內的全部整數
for a in range(1,3000):
    b = 0 
    i = 1 
    while i<= (a//2):
        if a %i == 0:
            b+= i 
        i+= 1
    # 計算b的個因子，將個因子之和存於n
    n = 0
    j = 1
    while j <= (b//2):
        if b%j == 0:
            n+= j
        j+= 1
    if n==a and a<b:
        print("%4d -- %4d\t"%(a,b))

