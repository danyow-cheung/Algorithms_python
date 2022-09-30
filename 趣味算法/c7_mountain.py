'''問題描述【搬山遊戲】
设有n座山，计算机与人作为比赛的双方，轮流搬山。规定每次 搬山数不能超过k座，
谁搬最后一座谁输。游戏开始时，计算机请人 输入山的总数n和每次允许搬山的最大数k，
然后请人开始，等人输 入了需要搬走的山的数目后，计算机马上打印出它搬多少座山，
并提示尚余多少座山。双方轮流搬山直到最后一座山搬完为止。计算 机会显示谁是赢家，
并问人是否要继续比赛。
如果人不想玩了，计 算机便会统计出共玩了几局，双方胜负如何。
'''

if __name__ =="__main__":
    pc = cc = 0 
    g = 1 
    while True:
        
        print("第%2d回合 " %g)
        print("---------------------")
        print("輸入一共有多少座山 ", end="")
        n = int(input())
        if not n:
            break
        # 允许的最大搬山数
        k = int(input("每次允許拿取的山數是 = ")) 
        while(k > n or k < 1):
            if k > n or k < 1:
                print("重複")
        while n:
            x = int(input("一次搬 = 山"))
            if x<1 or x>k or x>n:
                print("IIIegal,again please!")
                continue
            n -=x 
            print("There are %d mountains left now." %n)
            if not n:
                print("...............I win. You are failure...............")
                cc += 1
            else:
                y = (n-1)%(k+1)
                if not y:
                    y =1 
                n -= y 
                print("Copmputer move %d mountains away." %y)
                if n:
                    print(" There are %d mountains left now."  %n)
                else:
                    print("...............I am failure. You win..................")
                    pc += 1
        g+=1
    print("Games in total have been played %d." %(cc + pc)) 
    print("You score is win %d,lose %d." %(pc, cc)) 
    print("My score is win %d,lose %d." %(cc, pc))

                