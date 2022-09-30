'''問題描述【魔方陣】

所谓“n-魔方阵”，指的是使用l~n2 共n2 个自然数排列成一 个n×n的方阵，
其中n为奇数。该方阵的每行、每列以及对角线元素之和都相等，
并为一个只与n有关的常数，该常数为n×(n2 +1)/2。
'''

def array(n):
    # n是偶數，則加1使其變為奇數
    if n%2 ==0:
        n = n+1 
    max = n*n 
    mtrx = [1]*max
    mtrx[n//2] =1 
    # 自然數1所在行 
    i = 0 
    # 自然數1所在列 
    j = n//2 
    # 從2開始確定每個數的存放位置
    for num in range(2,max+1):
        i = i-1 
        j = j+1 
        # 当前数是n的倍数
        if (num -1)%n ==0:
            i = i+2 
            j = j-1 
        # 当前数在第0行
        if i<0:
            i = n-1 
        # 当前数在最后一列，即n-1列
        if j>n-1:
            j = 0 
        # 找到当前数在数组中存放的位置
        no = i*n+j 
        mtrx[no] = num 
    #打印生成魔方陣
    print("生成的%d-魔方阵为:" %n, end="")
    no = 0 
    for i in range(0,n):
        print()
        for j in range(0,n):
            print("%3d"%mtrx[no],end=" ")
            no+=1 
    print()

# if __name__=='__main__':
#     n = int(input("请输入n值:")) 
#     array(n)

    
'''問題擴展：使用二維數組生成5-魔方陣'''
def array_2():
    N = 5 
    # 定義一個5x5的二維數組
    a =[[0]*5 for i in range(5)]
    
    # 自然數1所在行 
    i = 0 
    # 自然數1所在列 
    j = N//2

    t = N-1 
    k =1 
    # 变量k控制循环和自然数
    while k<= (N*N):
        a[i][j]=k 
        # 變量x保存新的行
        x= i 
        # 變量y保存新的列
        y = j 
        # 當前數在第0行，則下一個數在最後一行
        if i==0:
            i = t 
        # 產生行，非0行，則取下一列
        else:
            i = i-1 
        # # 产生列，非最后列，则取下一列
        if j!= t:
            j = j+1 
        # 當然數在最後一列，則下一個數在第一列
        else:
            j = 0
        if a[i][j]!=0:
            i =x+1 
            j = y 
        k+= 1
    # 打印生成的魔方阵 print("生成的5-魔方阵为:", end="") 
    for i in range(N):
        print()
        for j in range(N):
            print("%3d " %a[i][j], end=" ")
    print()


# array_2()