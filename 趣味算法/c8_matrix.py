'''問題描述
编写一个程序，将一个3行3列的矩阵进行转置
'''

'''算法設計
解决矩阵问题时通常都是先将矩阵存放在一个二维数组中，而
当矩阵发生变化时，二维数组中对应的元素也会发生变化。

對角線上發生改變
'''

# if __name__ =="__main__":
#     n = [[1,2,3],[4,5,6],[7,8,9]]
#     print("原始矩陣")
#     for i in range(3):
#         for j in range(3):
#             print("%d "%(n[i][j]),end=" ")
#         print()
    
#     for i in range(3):
#         for j in range(3):
#             #将主对角线右上方的数组元素与主对角线左下方的数组元素进行单方向交换 
#             if j > i:
#                 temp = n[i][j]
#                 n[i][j] = n[j][i]
#                 n[j][i] = temp
        
#     print("轉置矩陣: ")
#     for i in range(3):
#         for j in range(3):
#             print("%d  " %(n[i][j]), end=" ")
#         print()

'''問題擴展
已知有一个3×4的矩阵，要求编程求出其中值最大及最小的元素所在的行号和列号，以及该元素的值。
'''

if __name__=="__main__":
    row1,row2 = 0,0 
    column1,column2 = 0,0
    a=[[12,17,13,16],[18,11,19,15],[10,14,12,15]]
    print("原始矩陣")
    for i in range(3):
        for j in range(4):
            print("%d "%(a[i][j]),end=" ")
        print()
    # 設置max的初值
    max = a[0][0]
    # 設置min的初值
    min = a[0][0]
    # 矩陣中每個元素逐一於max比較
    for  i in range(3):
        for j in range(4):
            if a[i][j]>max:
                max =a[i][j]
                row1 = i 
                column2 = j 

            if a[i][j]<min:
                min = a[i][j]
                row2 = i 
                column2 = j 

    print("矩阵的最大值为:%d，其所在行为第%d行，所在列为第%d列\n" %(max, row1, column1))
    print("矩阵的最小值为:%d，其所在行为第%d行，所在列为第%d列\n" %(min, row2, column2))