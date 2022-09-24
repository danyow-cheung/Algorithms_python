'''问题描述【大奖赛】
10个评委打分，去除最高分和最低分，其余求平均'''

'''算法设计【确定变量初值】
max--尽量小
min--尽量大
'''
# if __name__ =="__main__":
#     max = 0 
#     min = 100 
#     sum = 0 
#     for i in range(1,11):
#         print("第%d打分为："%i,end='')
#         integer = int(input())
#         if integer<0 or integer>100:
#             print("输入有错")
#             exit()
#         sum+= integer
#         if integer>max:
#             max = integer
#         if integer<min:
#             min = integer
        
#     print(f"最高{max}")
#     print(f"最低{min}")
#     final = (sum-max-min)//8
#     print(f"最后得分{final}")

'''问题扩展
找出评委分数中最公平（接近平均分）和最不公平（最不接近平均分）的分数
'''
import random
# 求出最大分数
def maxScore(score):
    max = score[0]
    # m是记录最大值的下标
    m = 0 
    for j in range(1,10):
        if max<score[i]:
            max = score[j]
            m = j 
    print("最大分数为%d"%max)

    return max,m 

# 求出最小分数
def minScore(score):
    min = score[0]
    # 记录下标
    n = 0 
    for j in range(1,10):
        if min>score[j]:
            min = score[j]
            n = j 
    print("最小分数为%d"%min)

    return min,n 


if __name__ =="__main__":
    sum = 0 
    score = [0]*10 
    for i in range(10):
        # 随机生成
        score[i] = random.randint(0,101)
        sum = sum + score[i]
    print(f"score = {score}")
    max,m = maxScore(score)
    min,n = minScore(score)

    avg = (sum - max-min)//8 
    # temp用来记录最公平与最不公平评委存储下标
    temp = 0 
    # s记录评分与平均值差值的绝对值
    s = abs(score[0] - avg)
    for i in range(10):
        if abs(score[i] - avg)==0:
            temp = i 
            print("最公平的评委是:%d, 打分:%d" % ((temp + 1),(score[temp+1])))
    temp = 0 
        
    for i in range(10):
        if abs(score[i] - avg) != 0:
            if s > abs(score[i] - avg):
                s = abs(score[i] - avg)
                temp = i 
    print("最公平的评委是:%d" %(temp + 1))

    if (avg - min) == (max - avg): 
        print("最不公平的评委是:%d %d" %((m+1), (n+1)))
    else:
        if (avg - min) > (max - avg):
            print("最不公平的评委就是:%d" %(n+1)) 
        else:
            print("最不公平的评委就是:%d" %(m+1))

