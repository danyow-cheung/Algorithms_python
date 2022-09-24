'''问题描述【計算分數的精確值】
使用数组精确计算M/N(0<M<N≤100)的值。假如M/N是无限循环小数，
则计算并输出它的第一循环节，
同时要求输出循环节的起 止位置(小数位的序号)。
'''

'''問題分析
因為計算機的字長限制，將商存放在一位數組中，
數組中的每個元素存放一位十進制數
既商的第一位存放在第一個元素中，商的第二位存放在第二個元素中

當計算後的余數為0，表示是有限不循環小數
余數和之前的某個余數相同時，則為無限循環小數
'''


'''算法分析
分 别定义两个数组remainder[101]和quotient[101]，
用来存放运算 过程中每一步的余数，及得到的每一位商。
'''


if __name__ =="__main__":
    # remainder 存放除法的余數
    remainder = [0]*101 
    # quotient依次存放商的每一位數
    quotient = [0]*101 
    print("請輸入分子於分母大於0，小於等於100的分數")
    m = int(input("分子 m = "))
    n = int(input("分母 n = "))
    print("%d/%d 的准确值是:0." %(m, n), end="")
    # i=商的位數
    for i in range(1,101):
        # m得到的余數：remainder[m]：該余數對應商的位數
        remainder[m] = i
        # 余數擴大10倍
        m*= 10
        # 商
        quotient[i] = m//n 
        # 求余數
        m = m%n 
        # 余數為0則表示是有限小數
        if m==0:
            j =1 
            while j<= i:
                # 輸出商
                print("%d" %quotient[j], end="")
                j += 1
            break
        # 若余數對應的位在前面出現過
        if remainder[m]!=0:
            j = 1
            while j<=i:
                # 輸出循環小數
                print("%d" %quotient[j], end="")
                j+= 1
            print("\n分数的第一个循环节:%d" %remainder[m]) 
            print("循环节的起始位置为:%d" %i)
            break