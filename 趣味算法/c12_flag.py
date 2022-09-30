'''問題描述【三色旗】

  假设有一条绳子，上面有红、白、蓝三种颜色的旗子。开始时
绳子上旗子的颜色并没有顺序，现在要对旗子进行分类，并按照
蓝、白、红的顺序排列。需要注意的是只能在绳子上进行移动，并
且一次只能调换两个旗子，则如何移动才能使旗子移动的次数最
少。
'''
# 交換棋子
def SWAP(x,y):
    temp = color[x]
    color[x] = color[y]
    color[y] = temp 

if __name__ =="__main__":
    WHITE ='W'
    RED = 'R'
    BLUE = 'B'
    color = ['R', 'W', 'B', 'W', 'W', 'B', 'R', 'B', 'W', 'R']
    # 定義字符數組
    w,b,r = 0,0,len(color)-1 

    # 打印出移動繩子上的棋子顏色
    for i in range(len(color)):
        print(color[i],end="")
    print()

    # 移動過程
    while w <=r :
        # 遇到白棋
        if color[w] == WHITE:
            w += 1 
        # 遇到的是蓝旗
        elif color[w] == BLUE:
            SWAP(b, w)
            b += 1
            w += 1
        # 遇到紅旗
        else:
            # 移动红旗指针使其指向当前最靠前的非红旗位置
            while w <r and color[r] ==RED:
                r -=1 
            SWAP(r,w)
            r -= 1 
    # 打印出移动后绳子上旗子的颜色 
    for i in range(len(color)):
        print(color[i], end=' ')
    print()