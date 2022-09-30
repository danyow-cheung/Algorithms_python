'''問題描述【角谷猜想】

角谷猜想的内容是任给一个自然数，
若为偶数则除以2，若为奇 数则乘以3再加1，
这样得到一个新的自然数之后再按照前面的法则继续演算，
若干次以后得到的结果必然为1。
在数学文献里，角谷猜 想也常常被称为“3X+1问题”。
请编程验证角谷猜想。
示例
6→3→10→5→16→8→4→2→1。
'''
if __name__ =="__main__":
    count = 0 
    n = int(input("請輸入一個自然數："))
    while n!=1:
        if n%2==1:
            n = n*3 +1 
            count += 1
            print("[%d]:%d*3+1=%d"%(count,(n-1)//3,n))
        else:
            n //=2 
            count +=1 
            print("[%d]:%d/2 =%d"%(count,2*n,n))
            
