'''問題描述【擲骰子】

骰子是一个有6个面的正方体，每个面分别印有1~6个小圆点代 表点数。
假设这个游戏的规则是两个人轮流掷骰子6次，并将每次投 掷的点数累加起来，点数多者获胜，
点数相同则为平局。
要求编写程序模拟这个游戏的过程，并求出玩100盘之后谁是最 终的获胜者。


'''
import random
import time 

if __name__=="__main__":
    # c1,c2分別記錄兩個人的獲勝盤數
    c1,c2 = 0,0 
    print("擲骰子100次")
    for i in range(1,101):
        d1,d2 = 0,0 
        for j in range(1,7):
            d1 = d1+random.randint(1,6)
            d2 = d2+random.randint(1,6)
        if d1>d2:
            c1+=1
        else:
            if d1<d2:
                c2+=1
    print("等待结果......") 
    time.sleep(5) 
    print("100次之后，获胜者是:") 
    if c1 > c2:
        print("第一个人获胜!")
    else:
        if c1 < c2: 
            print("第二个人获胜!")
        else:
            print("兩人平局")