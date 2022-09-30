'''問題描述【馬踏棋盤】
国际象棋的棋盘为8×8的方格棋盘。现将“马”放在任意指定 的方格中，
按照“马”走棋的规则将“马”进行移动。要求每个方 格只能进入一次，
最终使得“马”走遍棋盘的64个方格。编写一个 Python程序，实现马踏棋盘操作，
要求用1~64这64个数字标注 “马”移动的路径，
也就是按照求出的行走路线，将数字1~64依次 填入棋盘的方格中，并输出。
'''

'''算法設計
解决马踏棋盘问题的一种比较容易理解的方法是应用递归的深 度优先搜索的思想

因此在设计“马踏棋盘”的算法时可以借鉴图的深度优先遍历
算法和二叉树的先序遍历(根左右)算法

'''

# 深度优先搜索地"马踏棋盘"
def TravelChessBoard(x, y, tag):
    x1, y1, flag, count = x, y, False, 0
    chess[x][y] = tag
    if tag == 60:  # 搜索成功，返回1
        return True
    flag, x1, y1 = nextxy(x1, y1, count)  # 找到基于(x1,y1)的下一个可走位置
    while not flag and count < 7:  # 上一步未找到，则在其余几种可走位置中寻找下一个可走位置
        count = count + 1
        # print('(1): ', count)
        flag, x1, y1 = nextxy(x1, y1, count)

    while flag:  # 找到下一个可走位置，则进行深度优先搜索
        if TravelChessBoard(x1, y1, tag + 1):  # 递归
            return True
        x1 = x
        y1 = y
        count = count + 1
        flag, x1, y1 = nextxy(x1, y1, count)  # 寻找下一个(x,y)
        while not flag and count < 7:  # 循环地寻找下一个(x,y)
            count = count + 1
            # print('(2): ', count)
            flag, x1, y1 = nextxy(x1, y1, count)

    if not flag:
        chess[x][y] = 0  # 搜索不成功，擦除足迹，返回0
    return False


#  找到基於(x,y)位置的下一個可走的位置
def nextxy(x,y,count):
    # 找到坐標(x+2,y-1)
    if count==0 and x+2<= x-1 and y-1 >= 0 and chess[x+2][y-1]==0:
        x = x+2 
        y = y-1 
        flag =True 
    # 找到坐標(x+2,y+1)
    elif count ==1 and x+2<=x -1 and y+1<=Y-1 and chess[x+2][y+1]==0:
        x = x+2 
        y = y+1 
        flag =True 
    # 找到座標(x+1,y-2)
    elif count ==2 and x+1<=x -1 and y-2>=0 and chess[x+1][y-2]==0:
        x = x+1 
        y = y-2 
        flag =True 
    
    elif count == 3 and x + 1 <= X - 1 and y+2 <= Y-1 and chess[x+1][y+2] == 0: 
        x =x + 1
        y =y + 2 
        flag = True

    elif count == 4 and x - 2 >= 0 and y - 1 >= 0 and chess[x - 2][y - 1] == 0: 
        x =x - 2
        y =y - 1 
        flag = True
  
    elif count == 5 and x - 2 >= 0 and y + 1 <= Y - 1 and chess[x - 2][y +1] == 0: # 找到坐 标(x-2,y+1)
        x =x - 2
        y =y + 1 
        flag = True
        
    elif count == 6 and x - 1 >= 0 and y - 2 >= 0 and chess[x - 1][y - 2]== 0:  
        x =x-1 
        y = y-2                                                                     #
        flag = True
       
    elif count == 7 and x - 1 >= 0 and y + 2 <= Y - 1 and chess[x - 1][y +2] == 0: 
        x =x - 1
        y =y + 2 
        flag = True
    else:
        flag = False
    return flag, x, y

if __name__ =="__main__":
    X = 8
    Y = 8 
    # 初始化
    chess = [[0]*X for i in range(Y)]
    if TravelChessBoard(2,0,1):
        for i in range(X):
            for j in range(Y):
                print("%-5d" % chess[i][j],end="")
            print()
        print("The horse has travelled the chess borad")
    else:
        print("The horse cannot travel the chess board")