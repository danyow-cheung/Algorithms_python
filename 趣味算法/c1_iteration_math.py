# Newton Iteration Method for Solving Equation Roots
# 牛顿迭代法求方程根
# 编写用牛顿迭代法求方程根的函数。方程为
#           a^3+b^2+cx+d=0，
# 系数a、b、c、d由主函数输入，求x在1附近的一个实根。求出根后，由主函数输出

# 根据公式进行求解 --就算本人做数学也不一定懂

'''函数功能是牛顿迭代法求方程的根'''
def solution(a,b,c,d):
    x = 1.5,
    x0 =x 
    # 用所求得x的值替代x0原来的值
    # f用来描述方程的值，fd用来描述方程求导之后的值
    # f = a * x0 * x0 * x0 + b * x0 *x0+c*x0+d
    f = a * x0^3 + b * x0^2+c*x0+d
    fd = 3*a*x0^2 + 2*b*x0+c 
    # 函数增量
    h = f / fd 
    x = x0 -h 
    #  求得更接近方程的x的值
    while abs(x-x0)>= 1e-5:
        x0 = x 
        f = a*x0*x0*x0 + b*x0*x0+c*x0+d
        fd = 3*a*x0*x0 + 2*b*x0+c 
        h = f / fd 
        x = x0 -h
    # 返回
    return x 



if __name__ =="__main__":
    # 输入方程的系数
    print("请输入系数")
    a,b,c,d = map(float,input().split())
    
    # 用牛顿迭代法求方程的根
    x = solution(a,b,c,d)

    # 输出所求方程的根
    print("final = %.6f"%x)