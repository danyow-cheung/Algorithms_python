'''問題描述【求符合要求的素數】
编写程序实现将大于某个整数n且紧靠n的k个素数存入某个数组 中，
同时实现从infile.txt文件中读取10对n和k的值，
分别求出符 合要求的素数，并将结果保存到outfile.txt文件中。
'''
# 判斷素數
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False 
    return True 

# 求出緊靠n的k個素數
def num(n,k,array):
    i,n = 0,n+1 
    while k>0:
        if isPrime(n):
            array[i] = n 
            i+=1 
            k-=1 
        n+=1 

# 文件操作

if __name__ =="__main__":
    array = [0]*1000
    print('输入整数n和k:')
    n, k = map(int, input().split())
    num(n, k, array)
    for n in range(k):
        print(array[n], end=' ')
    print('\n')
