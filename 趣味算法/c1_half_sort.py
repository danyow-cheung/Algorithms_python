'''问题描述
折半查找本质是分治算法
只适用于有序序列
'''
'''算法步骤
使用左右指针，表示查找范围的上下界，mid代表中间位置
'''

if __name__ =="__main__":
    a = [-3,4,7,9,13,45,67,89,120,132]
    low = 0
    high = len(a) -1 
    
    # 记录下标,存储下标的位置
    k = -1 

    print("原来数据列为\n",a)
    m = int(input("输入查找的数据 m = "))
    
    '''折半查找'''
    # 额外情况也要考虑清楚，比如low=high的时候就是找到了
    while low <= high:
        mid = (low +high)// 2
        if m > a[mid]:
            low = mid+1
        else:
            if m<a[mid]:
                high = mid-1 
            else:
                # 都找不到
                k = mid 
                break

    if k>= 0:
        print("m = %d ,index = %d"%(m,k))
    else:
        print("not found ")

    '''问题扩展
    顺序查找
    从线性表第一个元素开始，依次与线性表中的各个元素进行比较，直到找到否则即为失败'''
    i = 0 
    while i<len(a):
        if m==a[i]:
            # k用来存储下标的捏
            k = i 
            break
        i+= 1
    if k>= 0:
        print("m = %d ,index = %d"%(m,k))
    else:
        print("not found ")
    

        
    