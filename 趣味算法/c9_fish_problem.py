'''問題描述【遞歸解決分魚問題】

A、B、C、D、E这5个人合伙夜间捕鱼，凌晨时都已经疲惫不 堪，
于是各自在河边的树丛中找地方睡着了。第二天日上三竿时， 
A第一个醒来，他将鱼平分为5份，把多余的一条扔回河中，
然后拿 着自己的一份回家去了;
B第二个醒来，但不知道A已经拿走了一份 鱼，于是他将剩下的鱼平分为5份，
扔掉多余的一条，然后只拿走 了自己的一份;
接着C、D、E依次醒来，也都按同样的办法分鱼。 
问这5个人至少合伙捕到多少条鱼?每个人醒来后所看到的鱼是多 少条?
'''

# 分魚遞歸方法
# n和x。
# n表示参与分鱼的人数，
# x表示n个人分鱼前鱼的总条数。
def fish(n,x):
    if (x-1)%5==0:
        if n==1:
            return 1 
        else:
            return fish(n-1,(x-1)//5*4)

if __name__=="__main__":
    i = 0 
    flag =  0
    while True:
        if flag !=1:
            i+=1 
            # x最小值位6，以後每次增加5
            x = i*5 +1 
            if(fish(5,x)):
                flag = 1 
                print("五个人合伙捕到的鱼总数为%d" %x)
                exit(0)
                