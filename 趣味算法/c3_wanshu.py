'''問題描述【完數】
如果一个数等于它的因子之和，
则称该数为“完数”（或“完全数”）
。例如，6的因子为1、2、3，而6=1+2+3，因此6是“完数

：因子是所有可以整除這個數的數
'''
'''問題分析
解决本题的关键是计算出所选取整数i（i的取值范围不固定）
的因子（因子就是所有可以整除这个数的数），
然后将各因子累加到变量s（记录所有因子之和），
若s等于i，则可确认i为完数，反之则不是完数。
【查看一個數j是不是i的因子，利用語句if i%j==0判斷】

'''



if __name__ =="__main__":
    # 
    n = int(input("請輸入所選範圍上限"))
    i= 2 
    while i<n:
        # s是累加因子之和，保證每次循環時s的初值為0
        s = 0
        # j控制除數範圍
        j = 1
        for j in range(i):
            # 判斷j是不是i的因子
            if j!= 0 and i%j==0:
                s+=j # 因子和
        # 判斷因子和是否與原數相等
        if s==i:
            print("2到%d之間的完數:%d"%(n,i))
        i+= 1
    
'''問題擴展
對於整數來說，其最大因子是n/2(此時n為偶數，若n為奇數最大因子小於n/2+)
所以可以把循環範圍縮小到1～n-1
'''
while i <n:
    s = 0
    j = 1 
    while j <= (n/2):
        if j!= 0 and i%j ==0:
            s+=j
        j+= 1
    if s==i:
        print(n,i)
    i+= 1
    