'''問題描述【將真分數分解為埃及分數】
真分数（a proper fraction）是指分子比分母小的分数

分子是1的分数，叫单位分数。古代埃及人在进行分数运算时
只使用分子是1的分数，因此这种分数也叫作埃及分数
'''
if __name__ =="__main__":
    print("請輸入一個分數")
    a,b = [int(i) for i in input().split()]
    print("輸入分數為:%ld/%ld"%(a,b))
    print("埃及分數:")
    while 1:
        # 若分子不能整除分母，則分解出一個分母為b//a+1 的埃及數
        if b % a != 0:
            c = b//a + 1 
        else:
            c = b//a
            a = 1
        if a==1:
            print("1/%ld\n"%c,end='')
        else:
            print("1/%ld +"%c,end='')
        # 求出餘數的分子
        a = a*c - b
        # 求出餘數的分母
        b = b*c 
        # 若餘數分子為3，分母為偶數，則輸出最後兩個埃及數
        if a==3 and b%2 ==0:
            print("1/%ld + 1/%ld\n"%(b//2,b))
            break



