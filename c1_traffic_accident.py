# 前两位数字相同，后两位数字相同
# 组合起来各不相同，并且是某数的平方

temp = int(input("输入车牌号"))
flag = 0 
for i in range(10):
    for j in range(10):
        '''穷举前两位和后两位数字'''
        if i != j:
            '''不相同才继续'''
            # 这一步代表的含义是按数位累加，相加之后才能用平方计算
            k = 1000*i+100*i+10*j+j
            '''判断k是不是某个整数的平方，是就输出'''
            # 优化算法，从（31开始，因为30之前数字平方小于4）
            for temp in range(31,100):
                if temp * temp == k:
                    print(k)
                    flag = 1
                    break

        