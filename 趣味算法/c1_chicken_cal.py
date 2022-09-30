'''
百钱买百鸡 有多少种情况
公鸡5元
母鸡3元
三只小鸡1元
'''
# 把公鸡、母鸡和小鸡的数量分别设为cock、hen、chicken，
# 则cock+hen+chicken=100，因此百钱买百鸡问题就转化成解不定方程组
'''对于不定方程组，可以利用穷举循环'''
cock = 0
while cock <= 20:
    hen = 0 
    while hen <= 33:
        chicken = 0
        while chicken <= 100:
            # 条件控制，总数量为100,钱也为100
            if (5*cock + 3*hen + chicken/3.0)== 100 and (hen+cock+chicken==100):
                print(f"母鸡:{hen}公鸡:{cock}小鸡:{chicken}\n")
            chicken += 1
        hen += 1
    cock+= 1


'''优化算法,当cock的数量确定，chicken的数量就是100-cock-hen,使用两层循环就好了'''
while cock <= 20:
    hen = 0 
    while hen <= 33:
        hen = 0
        chicken = 100-cock-hen
        if (5*cock + 3*hen + chicken/3.0)== 100:
            print(f"母鸡:{hen}公鸡:{cock}小鸡:{chicken}\n")
        hen += 1
    cock+= 1



