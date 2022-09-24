'''问题描述【誰家孩子跑最慢】
假设有张、王、李三家，每家都有3个孩子。某一天，
这三家的 9个孩子一起短跑比赛，规定不考虑年龄大小，第一名得9分，第二 名得8分，
第三名得7分，以此类推。比赛结束后统计分数发现三家 孩子的总分是相同的，同
时限定这9个孩子的名次不存在并列的情 况，且同一家的孩子不会获得相连的名次。
现已知获得第一名的是李家的孩子，
获得第二名的是王家的孩子，要求编程求出获得最后 一名的是哪家的孩子。
'''
'''問題分析

1)参加比赛的一共有9个孩子，得分情况依次是从1~9分。由 此可知，该场比赛总共的分数为9+8+7+6+5+4+3+2+1=45分。
2)由于“比赛结束后统计分数发现三家孩子的总分是相同 的”，因此每家孩子的得分都为15分。
3)由于“获得第一名的是李家的孩子，获得第二名的是王家的 孩子”，因此可推知获得第三名的一定是张家的孩子，否则李家 (或王家)的孩子总分就会超过15分。
4)由于“这9个孩子的名次不存在并列的情况，且同一家的孩 子不会获得相连的名次”，因此可推知获得第4名的一定不是张家的 孩子。
'''

if __name__ =="__main__":
    # 定義列表，用來存儲各個孩子的分數
    score =[([0]*4) for i in range(4) ]
    #score[1]、score[2]和score[3]分别存放张家、王家和李家3个孩子的分数 
    #获得第一名的是李家的孩子，获得第二名的是王家的孩子
    #初始化三家孩子的最高分数值
    score[1][1] = 7 
    score[2][1] = 8
    score[3][1] = 9

    # 通過循環得到9個孩子的分數
    for zhang in range(4,6):
        for wang in range(4,7):
            for li in range(4,7):
                # 9個孩子名次不存在並列情況
                if zhang!=wang and li != zhang and li!= wang and 15 -zhang -score[1][1]!=15-wang-score[2][1] and 15-zhang-score[1][1] != 15-li-score[3][1] and 15-wang-score[2][1] != 15-li-score[3][1]:
                    score[1][2] = zhang 
                    score[1][3] = 15-zhang-7 
                    score[2][2] = wang 
                    score[2][3] = 15 -wang - 8 
                    score[3][2] = li 
                    score[3][3] = 15-li-9
    # 打印二維數組,输出各家孩子的分数
    print("array score:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(score[i][j], end=' ')
        print()
    # for循環每一個孩子的分數值，並將最後一名孩子所來自的家庭保存到index中
    for n in range(len(score)):
        for m in score[n]:
            if m==1:
                index = n 
    # 輸出最後一名的家庭
    if index == 1:
        print("The last one reached the end is a child from family Zhang.\n")
    elif index == 2:
        print("The last one reached the end is a child from family Wang.\n")
    else:
        print("The last one reached the end is a child from family Li.\n")