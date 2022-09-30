'''問題描述【pai的近似值】
使用蒙特卡罗法求π的近似值
'''
from random import random
import math 
if __name__ =="__main__":
    # 落入正方形的总的点数，此数越大，越逼近π的近似值
    DARTS = 300000000
    # 落入四分之一圆的点数
    hits = 0.0 
    for  i in range(1,DARTS+1):
        x = random()
        y = random()
        dist = math.sqrt(x**2+y**2)
        if dist <=1.0:
            hits = hits+1
    pi = 4*(hits/DARTS)
    print("pi的值{}".format(pi))

