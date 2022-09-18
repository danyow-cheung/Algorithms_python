'''问题描述
小明有5本新书，要借给A、B、C三位小朋友，若每人每次只能借1本，则可以有多少种不同的借法？
排列组合，从5个数中取3个不同数的排列组合的总数
使用穷举实现

'''
# 表示有效借阅次数 
i = 0
for x in range(1,6):
    for y in range(1,6):
        for z in range(1,6):  
            # if x != y != z 错误判别式，会产生80个
            if x != y and y!=z and x!= z :
                print(f"a:{x}b:{y}c:{z}",end=" ")
                i+= 1

print("有效借阅次数为",i)

'''问题扩展
如果前两个人所选书号相同
那么无论第三个人所选书号与前两人相同与否都是无效的借阅方法
因此在执行第三个循环之前可先判定前两人的编号是否相同，进而提高程序效率。
'''
i= 0 
a = 1
while a <= 5:
    b= 1
    while b<=5:
        c = 1 
        while c<=5 and a!=b:
            if a!= b and b!=c and a!=c:
                print(f"a:{a}b:{b}c:{c}",end=" ")
                i+= 1
            c+=1
        b+= 1
    a+= 1
print("有效借阅次数为",i)