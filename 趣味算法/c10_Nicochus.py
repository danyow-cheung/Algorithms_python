'''問題描述【尼科彻斯定理】
任何一个整数的立方都可以表示成一串连续的奇数的和
3^3 =7+9+11=27
4^3 =13+15+17+19=64
5^3 =21+23+25+27+29=125
'''

if __name__ =="__main__":
    # sum變量存放奇數的累加和，初值為0
    sum = 0 
    n = int(input("請輸入大於1的n的值: "))
    if n<=1:
        print("輸入的n值有誤")
        exit()
    # cube存放的立方，也可以寫成cube = n***3
    cube = n*n*n 
    # 外層循環通過累加來查找奇數序列
    i = 1 
    while i< cube:
        # 內層循環通過累加來查找奇數序列
        j = 1 
        while j < cube:
            sum += j 
            # 找到奇數序列
            if sum==cube:
                print("%d =%d+%d+...%d"%(cube,i,i+2,j))
            # 沒找到，退出內層循環，返回外層for循環
            if sum>cube:
                # sum重置為0，方便下次試探
                sum = 0 
                break
            j+=2 
        i+=2 
