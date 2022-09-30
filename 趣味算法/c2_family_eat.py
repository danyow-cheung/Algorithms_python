'''問題描述
30個人吃飯，花了50先令
每個男人吃飯花3，每個女人吃飯花2，每個小孩花1.問各有多少人'''
'''問題分析
x-male
y-female
z-child
可得出方程式
    x+y+z=30
    3x+2y+z=50
    2x+y=20
'''

number = 0

# 將變量x的可能取值帶入方程組
for x in range(0,10+1):
    y = 20 - 2*x
    z = 30-x-y 
    if 3*x + 2*y+z == 50:
        number+= 1
        print("%2d:%4d%5d%6d"%(number,x,y,z))
        
