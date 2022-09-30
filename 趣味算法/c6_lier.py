'''問題描述【誰在說謊】
现有张三、李四和王五三个人，张三说李四在说谎，李四说王
五在说谎，而王五说张三和李四两人都在说谎。要求编程求出这三
个人中到底谁说的是真话，谁说的是假话。
'''
if __name__ =="__main__":
    # x,y,z表示張三李四王五說話真假情況
    #1 -true，0-flase
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (x and(not y) or (not x) and y) and(y and (not z) or (not y) and z) and (z and x==0 and y==0 or (not z ) and x+y!=0):
                    a = '真' if x == 1 else '假' 
                    b = '真' if y == 1 else '假' 
                    c = '真' if z == 1 else '假' 
                    print("张三说的是" + a + "话") 
                    print("李四说的是" + b + "话") 
                    print("王五说的是" + c + "话")