'''問題描述【勾股數】
求100以內的所有勾股數
'''
# import math 
# if __name__ =="__main__":
#     count = 0 
#     print("100以內的勾股數: ")
#     # a,b,c分別代表三角形的三個邊
#     print("   a\tb\t c \t\t a \t b \t  c \t\t a \t  b\t  c \t\t a\t b\t  c")
#     # 求100以内的勾股数」
#     for a in range(1,101):
#         for b in range(1,101):
#             c = int(math.sqrt(a*a+b*b))
#             if c*c == (a*a+b*b) and (a+b>c)and (a+c>b)and(b+c>a) and c<100:
#                 print("%4d %4d %4d\t |" %(a, b, c), end="")
#                 count += 1
#                 if count % 4 == 0:
#                     print()
'''問題擴展
由于任何一个勾股数组(a,b,c)内的三个数同时乘以一个整数n得到的新数组(na,nb,nc)
仍然是勾股数，所以一般我们想找的是a、b、c互质的勾股数组。
关于这样的数组，比较常用也比较实用的方法有以下两种

【1】當a為大於1的奇數2n+1時，b=2n^2+2n,c=2n^2+2n+1
【2】當a為大於4的偶數2n時，b=n^2-1,c=n^2+1
'''
if __name__ =="__main__":
    a = int(input("請輸入一個a值"))
    # 輸入的a為奇數，則a = 2n+1,b=2n^2+2n,c=2n^2+2n+1 
    if a>3 and a%2 ==1:
        n = (a-1)//2 
        b = 2*n**2+2*n 
        c = 2*n**2+2*n+1
        print("%d%d%d\n"%(a,b,c))
    else:
        # 輸入a為偶數，則a = 2n,b=n**2-1,c=n**2+1 
        if a>= 3 and a%2==0:
            n = a//2 
            b =n**2-1
            c=n**2+1 
            print("%d%d%d\n"%(a,b,c))
        else:
            print("error")