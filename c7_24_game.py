'''問題描述【24點遊戲】
在屏幕上输入1~10范围内的4个整数(可以有重复)，对它们 进行加、减、乘、除四则运算后
(可以任意的加括号限定计算的优 先级)，寻找计算结果等于24的表达式。

例如输入4个整数4、5、6、7，可得到表达式:4*((5- 6)+7)=24。
这只是一个解，本题目要求输出全部的解。要求表达式 中数字的顺序不能改变
'''
'''問題分析
4^3 = 64種可能情況
'''
# 该函数的 作用是使用前两个参数指定的操作数进行第3个参数指定的运算，并 返回其运算结果。
def cal(x,y,op):
    if op==1:
        return x+y 
    elif op==2:
        return x-y 
    elif op==3:
        return x*y 
    elif op==4:
        return x/y 

# 對應的表達式類型
def calculate_model1(i,j,k,t,op1,op2,op3):
    r1 = cal(i,j,op1)
    r2 = cal(r1,k,op2)
    r3 = cal(r2,t,op3)
    return r3 
def calculate_model2(i,j,k,t,op1,op2,op3):
    r1 = cal(j,k,op2)
    r2 = cal(i,r1,op1)
    r3 = cal(r2,t,op3)
    return r3 

def calculate_model3(i,j,k,t,op1,op2,op3):
    r1 = cal(k,t,op3)
    r2 = cal(j,r1,op2)
    r3 = cal(i,r2,op1)
    return r3 

def calculate_model4(i,j,k,t,op1,op2,op3):
    r1 = cal(j,k,op2)
    r2 = cal(r1,t,op3)
    r3 = cal(i,r2,op1)
    return r3 

def calculate_model5(i,j,k,t,op1,op2,op3):
    r1 = cal(i,j,op1)
    r2 = cal(k,t,op3)
    r3 = cal(r1,r2,op2)
    return r3 


op = ['#',"+","-","*","/"]


# 尋找符合要求的表格
def get24(i,j,k,t):
    flag = False 
    for op1 in range(1,5):
        for op2 in range(1,5):
            for op3 in range(1,5):
                # 找到((A□B)□C)□D类型的表达式中符合要求的表达式
                if calculate_model1(i, j, k, t, op1, op2, op3) == 24:
                    print("((%d%c%d)%c%d)%c%d=24" % (i, op[op1], j, op[op2],k,op[op3],t))
                    flag =True 


                # 找到(A□(B□C))□D类型的表达式中符合要求的表达式
                if calculate_model2(i, j, k, t, op1, op2, op3) == 24:
                    print("(%d%c(%d%c%d))%c%d=24" % (i, op[op1], j, op[op2],k,op[op3],t))
                    flag = True

                if calculate_model3(i, j, k, t, op1, op2, op3) == 24:
                    print("%d%c(%d%c(%d%c%d))=24" % (i, op[op1], j, op[op2],k, op[op3], t))
                    flag = True
                if calculate_model4(i, j, k, t, op1, op2, op3) == 24:
                    print("%d%c((%d%c%d)%c%d)=24" % (i, op[op1], j, op[op2],k, op[op3], t))
                    flag = True

                if calculate_model5(i, j, k, t, op1, op2, op3) == 24:
                    print("(%d%c%d)%c(%d%c%d)=24" % (i, op[op1], j, op[op2],k, op[op3], t))
                    flag = True
    return flag

if __name__=="__main__":
    print("Please input four integer (1~10)")
    i, j, k, t = map(int, input().split())
    # 若輸入不合法則重新輸入
    if i < 1 or i > 10 or j < 1 or j > 10 or k < 1 or k > 10 or t < 1 or t >10:
        print("Input illege,please input again")
        i,j,k,t = map(int,input().split())
        i, j, k, t = map(int, input().split())
    if get24(i,j,k,t):
        pass 

    else:
        print("Sorry,the four integer cannot be calculated to get 24")
    

                
                
