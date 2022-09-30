'''問題描述【農夫過河】
一个农夫在河边带了一匹狼、一只羊和一棵白菜，他需要把这
三样东西用船带到河的对岸。然而，这艘船只能容下农夫本人和另
外一样东西。如果农夫不在场的话，狼会吃掉羊，羊也会吃掉白
菜。请编程为农夫解决这个过河问题。
'''
'''算法設計
使用遞歸
'''
def search(step):
    # 該步驟能使各均值為1，則輸出結果，進入回歸步驟
    if a[step][0] + a[step][1]+a[step][2]+a[step][3]==4:
        # 能夠輸出不同方案
        for i in range(step+1):
            print("east: ",end=" ")
            if a[i][0] ==0:
                print("Wolf",end=" ")
            if a[i][1] ==0:
                print("Goat",end=" ")
            if a[i][2] ==0:
                print("Cabbage",end=" ")
            if a[i][3] ==0:
                print("Farmer",end=" ")
            if a[i][0] and a[i][1]and a[i][2] and a[i][3]:
                print("None",end=" ")

            print(end ="  ")
            print("west: ",end="")
            if a[i][0] == 1:
                print("wolf", end='  ')
            if a[i][1] == 1:
                print('goat', end='  ')
            if a[i][2] == 1:
                print('cabbage', end='  ')
            if a[i][3] == 1:
                print('farmer', end='  ')
            if not (a[i][0] or a[i][1] or a[i][2] or a[i][3]):
                print('none', end='')
            print('\n')
            if i<step:
                print("         the %d time' % (i + 1))")
            if i>0 and i<step:
                if a[i][3] ==0:
                    print("     -----> farmer ", end='')
                    print(name[b[i]+1])
                else:
                    print("             <----- farmer", end='')
                    print(name[b[i]+1])

        print('\n\n\n')
        return 

    for i in range(step):
        # 該步於以前的步驟相同，取消操作
        if (a[i]==a[step]):
            return 
    # 若羊和農夫不在一起而狼和羊或羊和白菜在一起，則取消操作
    if a[step][1] != a[step][3] and (a[step][2] == a[step][1] or a[step][0] ==a[step][1]):  
        return 
    # 遞歸，從帶第一種對象開始依次向下循環，同時限定遞歸界線
    for i in range(-1,3):
        # 記錄農夫渡河方式
        b[step] = i 
        # 複製上一步狀態，進行下一步移動
        a[step+1]=a[step][:]
        # 農夫過去或者回來
        a[step+1][3] = 1 - a[step+1][3]

        if i==-1:
            # 進行第一步
            search(step+1)
        elif a[step][i]==a[step][3]:
            # 帶回該物
            a[step+1][i] = a[step+1][3]
            search(step+1)


if __name__ =="__main__":
    N = 15 
    a = [[0]*4 for i in range(N)]
    b = [0]*N 

    name = ['   ',"and wolf",'and goat',"and cabbage"]

    print(' 农夫过河问题，解决方案如下:\n') 
    search(0)