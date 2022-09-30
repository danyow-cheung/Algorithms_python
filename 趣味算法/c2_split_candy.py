'''问题描述【分糖果】
「10个小孩围成一圈分糖果
老师分给第1个小孩10块，第2个小孩2块，第3个小孩8块，第4个小孩22块，第5个小孩16块，
第6个小孩4块，第7个小孩10块，第8个小孩6块，第9个小孩14块，第10个小孩20块。

然后所有的小孩同时将手中的糖分一半给右边的小孩；糖块数为奇数的人可向老师要一块。
问经过这样几次后大家手中的糖一样多？每人各有多少块糖？

'''

'''算法设计
使用数组存放老师初始分配的糖果数量
'''
# sweet [0] = 10 老师分给第1个小孩10块
sweet = [10,2,8,22,16,4,10,6,14,20]

# 判断每个孩子手里的糖果数是否相同
def judge(candy):
    for i in range(0,10):
        if candy[0]!=candy[i]:
            return 1 
    return 0 

# 将孩子手里的糖果进行平分，如果是偶数则为一半，奇数加1之后再给
def giveSweets(sweet,j):
    t = [0]*10
    # 判断是否存在相同
    while (judge(sweet)):
        # 将糖果平分
        for i in range(0,10):
            if sweet[i] % 2 ==0:
                sweet[i] = sweet[i]//2
                t[i] = sweet[i]
            else:
                sweet[i] = (sweet[i] + 1)//2
                t[i] = sweet[i]
        # 将分出的一半糖果给右边孩子
        for n in range(0,9):
            sweet[n+1] = sweet[n+1] + t[n]
        sweet[0] += t[9]
        j += 1
        printResult(sweet,j)

def printResult(s,j):
    print("%4d"%j,end=' ')
    k = 0
    while k< 10:
        print("%4d"%s[k],end=" ")
        k+= 1
        j+= 1
    print()

if __name__ =="__main__":
    j = 0 
    for i in range(len(sweet)):
        print("%4d"%sweet[i],end=" ")
    print(" ")
    print("次数     糖果数")
    giveSweets(sweet,j)