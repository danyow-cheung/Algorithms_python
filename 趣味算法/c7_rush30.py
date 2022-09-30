'''問題描述【搶30】
由两个人玩“抢30”游戏，游戏规则是:第一个人先说“1”或 “1，2”，
第二个人要接着往下说一个或两个数，然后又轮到第一 个人，
再接着往下说一个或两个数。这样两人反复轮流，
每次每个 人说一个或两个数都可以，但是不可以连说三个数，
谁先抢到30， 谁得胜。
'''
# 定義輸入函數
import random

def input_num(t):
    a = int(input("please count: "))
    while a>2 or a<1 or a+t>30:
        if a>2 or a<1 or a+t>30:
            print("Error Input,again")
        else:
            print("You count:%d"%(t+a))
        a = int(input("please count: "))
    print("you count %d"%(t+a))
    # 返回當前已經取走的數的累加和
    return t+a 

# 計算誰會勝利
def copu(s):
    c = 0 
    print("Computer count: ",end="")
    if (s+1)%3 ==0:
        s = s+1 
        print(s)
    else:
        if (s+2)%3==0:
            s =s+1 
            print(s)
        else:
            c = random.randint(1,2)
            s = s+c 
            print(s)
    return s 


if __name__ =='__main__':
    tol = 0 
    print("***********catch thirty **************") 
    print("Game Begin")
    # 取随机数决定机器和人谁先走第一步。若为1，则表示人先走第一步
    if (random.randint(1, 2) == 1):
        tol = input_num(tol)
    while tol!= 30:
        tol = copu(tol)
        if tol==30:
            print("Computer:I Lose!")
        else:
            tol = input_num(tol)
            if tol==30:
                print("People: I lose !")
    