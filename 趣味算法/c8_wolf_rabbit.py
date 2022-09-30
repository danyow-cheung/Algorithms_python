'''問題描述【狼追兔子】

一只兔子躲进了10个环形分布的洞中的某一个
。狼在第一个洞 中没有找到兔子，就隔一个洞，
到第三个洞中去找;如果没有找 到，就隔两个洞，
到第六个洞中去找;以后每次多隔一个洞去找兔 子......
这样下去，如果一直找不到兔子，请问兔子可能在哪个洞 中?
'''

if __name__=="__main__":
    n = 0
    x = 0 
    # 定義一個長度為11的數組，初始值為1
    a =[1]*11 
    for i in range(0,1000):
        n += (i+1)
        x = n%10 
        a[x] = 0
    for i in range(0,10):
        if a[i]:
            print("可能在第%d个洞中" %i)