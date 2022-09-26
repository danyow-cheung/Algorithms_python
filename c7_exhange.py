'''問題描述【黑白子交换】
游戏的规则如下:
1)一次只能移动一个棋子。
2)棋子可以向空格中移动，也可以跳过一个对方的棋子进入空格
3)白色棋子只能向右移动，黑色棋子只能向左移动，不能跳过两个棋子。
'''
# 打印輸出結果
def printLine(a):
    global number 
    print("No.%2d:.........."% number)
    number +=1
    print(" ",end="")
    for i in range(7):
        if a[i]==1:
            print("|*",end="")
        else:
            if a[i]==2:
                print("|@",end="")
            else:
                print("| ",end="")
    print("|\n...............\n")

# 交換
def change(t,i,j):
    term = t[i]
    t[i] = t[j]
    t[j] = term 
    return t 


if __name__=="__main__":
    # 初始化數組，1代表白子，2代表黑子，0代表空格
    t = [1,1,1,0,2,2,2]
    number = 0
    printLine(t)
    # 若沒有完成棋子的交換則繼續進行循環
    # 判斷遊戲是否結束
    while t[0]+t[1]+t[2]!= 6 or t[4]+t[5]+t[6]!=3:
        # flag為棋子移動一步的標記，flag=True表示尚未移動棋子，flag=False表示已經移動棋子
        flag =True 
        i = 0 
        # 若白子可以向右跳過黑子，則白子向右跳
        while flag and i<5:
            if t[i]==1 and t[i+1]==2 and t[i+2]==0:
                # 調用交換
                t = change(t,i,i+2)
                printLine(t)
                flag = False 
            i+=1 
        i = 0 
        # 若黑子可以向左跳過白子，則黑子向左跳
        while flag and i <5:
            if t[i]==0 and t[i+1]==1 and t[i+2]==2:
                t = change(t,i,i+2)
                printLine(t)
                flag = False 
            i+= 1
        i = 0
        # 若向右移動白子不會產生阻塞，則白子向右移動
        while flag and i<6:
            f = True 
            if i<5:
                f = t[i-1]!=t[i+2]
            if t[i]==1 and t[i+1]==0 and (i==0 or f):
                t = change(t,i,i+1)
                printLine(t)
                flag = False 
            i+=1 
        i =0
        while flag and i < 6: # 若向左移动黑子不会产生阻塞，则黑子向左移动
                f = True
                if i < 5:
                    f = t[i - 1] != t[i + 2]
                if t[i] == 0 and t[i + 1] == 2 and (i == 5 or f):
                    t = change(t, i, i + 1)
                    printLine(t)
                    flag = False
        i += 1
