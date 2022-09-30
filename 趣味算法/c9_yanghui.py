'''問題描述【楊輝三角形】

杨辉三角形中的数，正是(x+y)的N次方幂展开式各项的系数。 
本题作为程序设计中具有代表性的题目，求解的方法很多，
下面以 递归的方法来打印杨辉三角形
'''

# 楊輝三角形遞歸三角形
def c(x,y):
    if y==1 or y==x:# y=1 或者y=x時。函數返回值為1
        return 1 
    else:
        z = c(x-1,y-1)+c(x-1,y)
        return z 
# 問題擴展：使用二維數組打印楊輝三角形

if __name__ =='__main__':
    n = int(input("請輸入楊輝三角形行數: "))
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print("  ",end=" ")
        for j in range(1,i+1):
            # 調用遞歸函數，輸出第i行的第j個值
            print("%6d "%(c(i,j)),end=" ")
        print()
    


