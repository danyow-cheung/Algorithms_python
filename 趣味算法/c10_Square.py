'''问题描述【四方定理】

四方定理是数论中的重要定理，
它可以叙述为“所有的自然数至多用4个数的平方和就可以表示出来”
25=1*1+2*2+2*2+4*4 
99=1*1+1*1+4*4+9*9 
要求编写程序来验证四方定理。
'''
if __name__ =="__main__":
    number = int(input("請輸入一個自然數"))
    # 窮舉各種情況
    for x1 in range(0,number//2):
        for x2 in range(0,x1+1):
            for x3 in range(0,x2+1):
                for x4 in range(0,x3+1):
                    # 判斷是否滿足定理要求
                    if number == x1*x1+x2*x2+x3*x3+x4*x4:
                    # 若滿足定理要求，則輸出其中一組解，並退出循環
                        print("%d=%d*%d+%d*%d+%d*%d+%d*%d" %(number, x1, x1,x2,x2,x3,x3,x4,x4))
                        exit(0)


                    