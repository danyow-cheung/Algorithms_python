'''问题描述
银行一年整存整取月息0.63%
某人决定在今后5年年底取出1000元，到第五年刚好取完，问存钱存了多少'''

'''分析步骤
第五年年初存款数量=1000/(1+12x0.63%)
第四年年初存款数量=(第五年年初存款+1000)/(1+12x0.63%)
第三年年初存款数量=(第四年年初存款+1000)/(1+12x0.63%)
第二年年初存款数量=(第三年年初存款+1000)/(1+12x0.63%)
第一年年初存款数量=(第二年年初存款+1000)/(1+12x0.63%)
'''
i = 0 
# 刚好取完的钱
money = 0
lixi = 1+ 0.0063 * 12 
while i <5:
    
    money = (money+1000)/lixi
    i+= 1
print("一开始存钱为",money)