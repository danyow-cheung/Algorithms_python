'''問題描述【多項式之和】
S= 1+(1/(1*2))+(1/(1*2*3))+....+(1/(1*2*3..*50))
'''

'''問題分析
【1】求出每項的階乘再將其倒數和加在一起即為所求多項式的結果
【2】後面一項等於前一項乘以當前項數的倒數，
如果这里的每一项都用同一个变量t表示，那么第i项就可以用公式
表示为t=t*1/i。这样可以只用一层循环来实现，循环变量i控制对应的项数，取值范围为1~n。'''


# 方法1
if __name__ =='__main__':
    n = int(input("請輸入一個整數n = "))
    # s記錄多項式的和
    s = 0 
    # i記錄對應的項數
    i = 1 

    while i <=n:
        # t記錄每一項分式的分母，每次循環前給t賦初值
        t = 1
        j = 1 
        while j <=i:
            t = t* j
            j += 1
        s = s+1/t 
        i += 1
    print("%f"%s)

# 方法2 
if __name__ =="__main__":
    n = int(input("請輸入一個整數n = "))
    # s記錄多項式的和
    s = 0 
    t = 1
    # i<= n,i控制對應的項數 
    for i in range(1,n+1):
        #將分式的值賦給變量t 
       t = t*1/i 
       s = s+t 
    print("%f"%s) 