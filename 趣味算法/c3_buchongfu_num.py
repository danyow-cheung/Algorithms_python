'''問題描述【不重複的3位數】
用1，2，3，4共4個數字能組成多少個互不相同且無重複數字的三位數
'''
if __name__ =="__main__":
    count = 0 
    for i in range(1,5):
        for j in range(1,5):
            k = 1 
            while k < 5 and i!= j:
                if k!=j and k!= i and i!= j:
                    print("%d%d%d"%(i,j,k))
                    count+= 1
                k+= 1

    print("總共有%d個"%count)