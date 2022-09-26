'''問題描述【自動發牌】
一副扑克有52张牌，打桥牌时应将牌分给4个人。
请设计一个程序完成自动发牌的工作。
要求:黑桃用S(Spaces)表示，
-红桃用H(Hearts)表示
-方块用D(Diamonds)表示，
-梅花用 C(Clubs)表示。
'''
import random 

def p(b,n):
    # 打印黑桃標記
    print("\n♠️",end="")
    # 將數組中值轉換為對應的花色
    for i in range(13):
        # 找到花色對應的牌
        if b[i]//13 ==0:
            print(n[b[i]%13],end="")
    # 打印紅桃標記
    print("\n♥️",end="")
    for i in range(13):
        if b[i]//13 ==1:
            print(n[b[i] %13],end="")
    # 打印方塊標記
    print("\n♦️",end="")
    for i in range(13):
        if b[i]//13 ==2:
            print(n[b[i] %13],end="")
    
    # 打印梅花標記
    print("\n♣️",end="")
    for i in range(13):
        if b[i]//13 ==3 or b[i]//13==4:
            print(n[b[i] %13],end="")
    
    print()

if __name__=="__main__":
    n = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    a = [0] * 53
    b1 = [0] * 13
    b2 = [0] * 13
    b3 = [0] * 13
    b4 = [0] * 13

    b11,b22,b33,b44,t = 0,0,0,0,1
    # 控制發牌52張
    while (t<=52):
        # 產生0-51之間的隨機數
        m = random.randint(0,52)
        flag ,i = True,1
        # 查找新產生的隨機數是否存在
        while i<= t and flag:
            if m==a[i]:
                # flag=1表示產生的是新的隨機數,flag=0s
                flag = 0 
            i+=1
        if flag:
            # 產生新的隨機數，存入數組
            a[t]=m 
            t+=1
            # 根據t的值，判斷當前的牌應存入哪個數組中
            if t%4==0:
                b1[b11]=a[t-1]
                b11+=1
            elif t%4==1:
                b2[b22]=a[t-1]
                b22+=1
            elif t%4==2:
                b3[b33]=a[t-1]
                b33+=1
            elif t%4==3:
                b4[b44]==a[t-1]
                b44+=1
        b1 = sorted(b1, reverse=True)
        b2 = sorted(b2, reverse=True)
        b3 = sorted(b3, reverse=True)
        b4 = sorted(b4, reverse=True)
        # 将每个人的牌进行排序
        p(b1, n)
        p(b2, n)
        p(b3, n)
        p(b4, n)
        
