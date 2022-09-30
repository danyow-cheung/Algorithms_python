'''問題描述【約瑟夫環】

程序从第一人开始对还未扔下海的人进行计数，
每数到9时，就 将数组中的标记改为0，
表示该人已经被扔下海了，如此循环计数直 到有15个人被扔下海为止。
'''

if __name__ =="__main__":
    # 30個人
    array = [[0]*2 for i in range(31)]
    print('最终结果为(s:被扔下海,b:在船上):')
    for i in range(1,31):
        # flag 標誌置1，表示人在船上
        array[i][0] = 1
        # next值為下一個元素的下標，既指向下一個人
        array[i][1] = i + 1 
    # 第30個人數組下標指向第一個人構成環
    array[30][1] =1 

    j = 30 
    # 循环变量i作为计数器，记录已扔下海的人数，共15个
    for i in range(15):
        k = 0 
        # 循环变量k作为计数器，决定哪个人被扔下海，计数到9为止
        while True:
            if k<9:
                # 修改数组下标，取下一个人
                j = array[j][1]
                # 进行计数，已扔下海的人标记为0
                k += array[j][0]
            else:
                break
        array[j][0] = 0
    

    for i in range(1,31):
        if array[i][0]:
            print("b",end="")
        else:
            print("s",end="")
    print()
