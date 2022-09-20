'''問題描述【水仙花數】
所谓的“水仙花数”是指一个三位数，其各位数字的立方和等于该数本身，例如，
153是“水仙花数” 因为153=1^3+1^3+3^3
'''
'''問題分析
把給出的三位數的個位，十位和百位分別拆分，並求其立方和(s)
如果s於給出的三位數相等，則該三位數為水仙花數
'''
print("水仙花數量")
for n in range(100,1000):
    hun = n//100
    ten = (n-hun*100)//10
    ind = n%10
    m =  hun*hun*hun + ten*ten*ten + ind*ind*ind
    if n == m:
        print(n)
    else:
        n+=1


'''問題擴展
冪運算**
m =  hun*hun*hun + ten*ten*ten + ind*ind*ind
更改為
m = hun**3 + ten**3+ind**3
'''
