'''問題描述【選美比賽】
一批选手参加比赛，比赛的规则是最后得分越高，名次越低。
当半决赛结束时，要在现场按照选手的出场顺序宣布最后得分和最
后的名次，获得相同分数的选手具有相同的名次，名次连续编号，
不用考虑同名次的选手人数。

'''

# 冒泡排序，排序後數組psn按照score的值從小到大排列
def sortScore(psn,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if psn[j][1]>psn[j+1][1]:
                # 交換psn[j]和psn[j+1]
                temp = psn[j]
                psn[j] = psn[j+1]
                psn[j+1]=temp 

# 指定每一位選手的名次
def setRand(psn,n):
    j =1 
    # 設定第一位選手的名次
    psn[0][2] = 1
    # 設定psn[2]~psn[n-1]名次
    for i in range(n):
        if(psn[i][1]!=psn[i-1][1]):
            psn[i][2]=j
            j+=1
        else:
            # psn[i]於psn[i-1]名次相同
            psn[i][2]=psn[i-1][2]


# 按照選手的序號重新排序，以便選手的序號輸出接過
def sortNum(psn,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if psn[j][0]>psn[j+1][0]:
                #交换psn[j]与psn[j+1]
                tmp = psn[j]
                psn[j] = psn[j+1]
                psn[j+1]=tmp 

def sortRand(psn,n):
    sortScore(psn,n)
    setRand(psn,n)
    sortNum(psn,n)
if __name__ == '__main__': #选手的信息组成一个结构体数组
    #以分数为关键字排序 #按照分数排名次 #按照序号重新排序
    psn = [[1, 5, 0], [2, 3, 0], [3, 4, 0], [4, 7, 0], [5, 3, 0], [6, 5, 0],[7, 6, 0]]
    sortRand(psn, 7)
    print("num score rand ") #输出结果
    for i in range(7):
        print("%d%6d%6d" % (psn[i][0], psn[i][1], psn[i][2]))