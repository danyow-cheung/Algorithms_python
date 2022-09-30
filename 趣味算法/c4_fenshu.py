'''问题描述【分数比较】
比较两个分数的大小
'''
'''问题分析
人工方式下比较分数大小最常用的方法是:进行分数的通分后
比较分子的大小。通分的步骤可描述如下:
1)先求出原来几个分数(式)的分母的最简公分母。
2)根据分数(式)的基本性质，把原来分数(式)化成以最简公分母为分母的分数(式)
'''

# 求出两个数的最大公约数
def common_divisor(a,b):
    # 先交换数字
    if a<b:
        temp = a 
        a = b 
        b = temp 
    #求分母a和b的最大公约数
    c = a*b 
    while b!= 0:
        d = b 
        b = a%b
        a =d 
    return c//a 

if __name__ =="__main__":
    print("请分别输入两个分数:")
    i, j = [int(i) for i in input("请输入第一个分数: ").split()] 
    k, l = [int(i) for i in input("请输入第二个分数: ").split()]

    print("第一个分数:%d/%d" %(i, j))
    print("第二个分数:%d/%d" %(k, l))
    #  求出第一个分数通分后的分子
    m = common_divisor(j, l) // j * i
    #  求出第二个分数通分后的分子
    n = common_divisor(j, l) // l * k
    if m>n:
        print("%d/%d > %d/%d"%(i,j,k,l))
    else:
        if m==n:
            print("%d/%d = %d/%d"%(i,j,k,l))
        else:
            print("%d/%d < %d/%d"%(i,j,k,l))