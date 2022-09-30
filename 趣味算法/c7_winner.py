'''問題描述【常勝將軍】
有火柴21根，两人依次取，每次每人只可取走1~4根，
不能多 取，也不能不取，谁取到最后一根火柴谁输。
请编写一个人机对弈 程序，要求人先取，计算机后取;计算机为“常胜将军”。
'''
if __name__=="__main__":
    spare = 21 
    while 1:
        print("火棍剩餘%d根"%spare)
        people = int(input("人取火棍 ="))
        if people<1 or people>4 or people>spare:
            print("你违规了，你取的火柴数有问题!")
            continue
        spare = spare-people
        # 人取后，剩余的火柴数为0，则计算机获胜，跳出循环
        if spare == 0: 
            
            print("计算机获胜，游戏结束!") 
            break
        # 计算机取火柴
        computer = 5 - people
        spare = spare - computer 
        print("计算机取火柴:%d" %computer) 
        # 计算机取后，剩余的火柴数为0，则人获胜，跳出循环
        if spare == 0: 
            print("人获胜，游戏结束!") 
            break
