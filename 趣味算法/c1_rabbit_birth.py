# 有一对兔子，从出生后到第三个月起每个月都生一对兔子
# 小兔子长到第三个月起每个月都生一对兔子，假设所有兔子都不死
# 问30个月内兔子总对数

# 本质为Fibonacci数，总结数列规律为前两个月的兔子对数为第三个月兔子的对数
# 数学公式：
    # 1. n<3.Bn-1 = Bn-1=1
    # 2. n>3.Bn = Bn-1+Bn-2
def Fibonacci():
    # 初始化兔子对数为1
    Fib1 = 1
    Fib2 = 1
    n = 3
    # 30个月
    while n <= 30:
        # 公式2.
        Fib = Fib1+Fib2 
        print('Fib',Fib)

        Fib2 = Fib1
        Fib1 = Fib 
        n+= 1


    # 改进算法，使用两个变量来实现，将Fib的内容放在Fib1中，代表最新的一个月的兔子对数
    # Fib2 = Fib2+Fib1 此时Fib1代表第三个月的数量，Fib2就是第4个月的数量

    Fib1 = 1 
    Fib2 = 1 
    i = 1
    while i<=15:
        # 每次求两个变量，所以循环次数减半
        print("Fib1",Fib1,"Fib2",Fib2)
        Fib1 = Fib1+Fib2 
        Fib2 = Fib2+Fib1 
        i+=1
Fibonacci() 


    