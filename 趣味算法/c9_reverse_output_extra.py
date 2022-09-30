'''問題描述【逆序輸出數字】
  编程实现将输入的整数逆序输出。
'''

# 逆序函數
def reverse(n):
    if n!=0:
        # 輸出正整數n當前的最高位置
        print("%d"%(n%10),end="")
        reverse(n//10)

'''問題擴展
【逆序輸出字符串】
'''
def reverse_str(s):
    if len(s)<=1:
        return s 
    return reverse_str(s[1:]) + s[0]
'''遞歸求最大公約數'''
def gcd(m,n):
    if n==0:
        g = m 
    else:
        g = gcd(n,m%n)
    return g 

if __name__=="__main__":
    # Problem 1
    # num = int(input("請輸入一個整數："))
    # # 如果num<0,先把num轉換為字符串，截取第一位-號,然後將數字逆序,再拼接上符號輸出
    # if num<0:
    #     str_num = str(num)
    #     # 減掉符號位
    #     num = str_num[1:]
    #     print("-",end="")
    #     reverse(int(num))
    # else:
    #     reverse(num)

    # Problem 2
    # num = input("請輸入一個整數：")
    # final = reverse_str(num)
    # print(final)

    #Problem 3 
    print("请输入两个正整数:")
    m = int(input("m = "))
    n = int(input("n = "))
    g = gcd(m, n) 
    print("%d和%d的最大公约数是:%d" %(m, n,g))

    

