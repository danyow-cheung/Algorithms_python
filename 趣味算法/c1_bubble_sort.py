'''🫧冒泡排序
两个相映元素进行交换的过程
n个元素的话 只比较n-1次
'''
# a=[1,43,234,64,2,5]
# n = len(a)

# # 第一次交换
# for j in range(0,n-1):
#     if a[j]>a[j+1]:
#         temp = a[j]
#         a[j] = a[j+1]
#         a[j+1] = temp 
# # 第二次交换（最后一个元素经过第一轮比较已经确定，不需要再次比较
# for j in range(0,n-2):
#     if a[j]>a[j+1]:
#         temp = a[j]
#         a[j] = a[j+1]
#         a[j+1] = temp 
# # 第三次交换（最后两个元素已经确定，不需要再次比较
# for j in range(0,n-3):
#     if a[j]>a[j+1]:
#         temp = a[j]
#         a[j] = a[j+1]
#         a[j+1] = temp


# 完整程序如下
def BubbleSort(a):
    # 获取列表的总长度
    n = len(a) 
    # 进行n-1次比较，控制比较的轮数
    i = 1
    while i <= n-1:
        j = 0 
        while j<n-i:
            if a[j]>a[j+1]:
                temp = a[j] 
                a[j] = a[j+1]
                a[j+1]=temp 
            j+= 1
        i+= 1

    # 打印每一轮交换后的列表
    for a1 in a:
        print(a1,end=" ") 

'''扩展内容
选择排序算法步骤:
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。
'''
def selectionSort(a):
    # 求出列表的长度
    n = len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[j]<a[i]:
                temp  = a[i]
                a[i] = a[j]
                a[j]=temp 
    
    for i in a:
        print(i,end=" ")


if __name__ =="__main__":
    print("为列表元素赋初值，列表末尾不能有空格")
    x = input()
    # 空格方式分割元素
    a = x.split()
    for i in range(0,len(a)):
        a[i] = int(a[i])
    print("输入列表为\n",a)
    print("冒泡排序之后为\n")
    BubbleSort(a)
    print("选择排序之后为\n")
    selectionSort(a)



