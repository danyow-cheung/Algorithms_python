'''問題描述【填表格】

将1、2、3、4、5和6填入下表中，
要求每一列右边的数字比左边的数字大
且每一行下面的数字比上面的数字大。
table 3X2 
编程求出共有几种填写方法?
'''
# 判斷a[1]-a[4]的值
def judge(b):
    for i in range(1,4):
        l = i+1
        while l<5:
            if (b[l]==b[i]):
                # 判斷值是否有重複
                return False 
            i+= 1
    # 若a[1]~a[4]的取值各不相同，则返回True
    return True

if __name__ =="__main__":
    # 計數器
    count = 1 
    # 初始化列表
    a = [1,2,3,4,5,6]
    print("滿足條件有")
    a[1] = a[0]+1 
    while a[1]<=5:
        a[2] =a[1]+1 
        while a[2]<=5:
            a[3] = a[0]+1 
            # 第二行的a[3]必须大于a[0]
            while a[3]<=5:
                # 第二行的a[4]必须大于左侧的a[3]和上边的a[1]
                if a[1]>a[3]:
                    a[4] = a[1]+1 
                else:
                    a[4] = a[3]+1 
                while a[4]<=5:
                    if judge(a):
                        # 如果有滿足題意，則打印結果
                        print('結果%d'%count)
                        count +=1 
                        print(a[:3])
                        print(a[3:])
                        print()
                    a[4]+=1 
                a[3]+=1 
            a[2] +=1 
        a[1]+=1 
    