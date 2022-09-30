'''问题描述【个人所得税】
·起征点为2000元。
·不超过500元的部分，征收5%。
·超过500～2000元的部分，征收10%。
·超过2000～5000元的部分，征收15%。
·超过5000～20000元的部分，征收20%。
·超过20000～40000元的部分，征收25%。
·超过40000～60000元的部分，征收30%。
·超过60000～80000元的部分，征收35%。
·超过80000～100000元的部分，征收40%
·超过100000元以上，征收45%
'''

'''基本知识
元组：元素一旦被确定就不能改变'''

'''算法设计
使用元组来存储每个金钱范围和利率的变化
'''
# 分为9个阶段，每个阶段第一个值为个税起征点，第二值为该阶段截止点，第三个值为税率
TaxTable = [ 
    (0,500,0.05),
    (500,2000,0.10),
    (2000,5000,0.15),
    (5000,20000,0.20),
    (20000,40000,0.25),
    (40000,60000,0.30),
    (60000,80000,0.35),
    (80000,100000,0.40),
    (100000,1e10,0.45)
]
'''定义计算税率的函数
profit-个人收入
TAXBASE-个税起征点
profit-TAXBASE个人收入超出个税起征点的部分，仍存入profit变量中
'''

def CaculateTax(profit):
    tax = 0.0 
    TAXBASE = 2000
    # 超过个税起点的收入
    profit -= TAXBASE 
    i = 0 
    for i in range(len(TaxTable)):
        # 判断profit是否在当前缴税范围内
        if (profit>TaxTable[i][0]):
            # profit超过当前缴税范围
            if (profit>TaxTable[i][2]):
                tax += (TaxTable[i][1]-TaxTable[i][0])*TaxTable[i][2]
            else:
                #profit没超过当前缴税范围
                tax += (profit-TaxTable[i][0])*TaxTable[i][2]
            profit -= TaxTable[i][1]
            if profit<0:
                profit = 0
            print(f"起征范围:{TaxTable[i][0]-TaxTable[i][1]} 缴税金额:{tax} 超过范围的金额{profit}")

    return tax 

if __name__=="__main__":
    profit = int(input("输入收入金额"))
    tax = CaculateTax(profit)
    print("个人所得税\n",tax)
