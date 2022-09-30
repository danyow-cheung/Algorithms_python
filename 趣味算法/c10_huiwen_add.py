'''問題描述【回文數的形成】
任取一个十进制正整数，将其倒过来后与原来的正整数相加，
会得到一个新的正整数，重复以上步骤，则最终可得到一个回文
数。请编程进行验证。
'''
# 求反序數
def reverse(a):
    t = 0 
    while a>0:
        # t存放的是a的反序數
        t = t*10+a%10
        a//=10
    return t 

# 判斷是否是回文數
def palindrome(s):
    # 調用reverese()函數判斷變量s是否與其反序數相等
    if (reverse(s)==s):
        return 1 
    else:
        return 0 

if __name__=="__main__":
    # 与C语言不同的是，Python支持大数计算，无限位数
    # 对于小整数，它会使用机器自身的整数计算功能去快速计算，当超出机器自身所能支持的范
    # 围时，自动转换为大数计算
    n = int(input("请输入一个正整数:"))
    print("回文数的产生过程如下:") 
    count = 0
    m = reverse(n)
    # 判斷是否為回文數
    while (palindrome(m+n)==0):
        count += 1
        # 打印步驟
        print("[%d]:%d+%d=%d"%(count,n,m,m+n))
        # n加上反序數
        n+= m
        m = reverse(n)
    count+=1 
    print("[%d]:%d+%d=%d\n"%(count,n,m,m+n))
    