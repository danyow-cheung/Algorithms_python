
'''
問題描述【雙色球】
编写程序模拟福利彩票的双色球开奖过程，由程序产生出6个红 色球和1个蓝色球。

1)每期开出的红色球号码不能重复，但蓝色球可以是红色球中 的一个。
2)红色球的范围是1~33，蓝色球的范围是1~16。 3)输出格式为“红色球:x x x x x x 蓝色球:x”。
'''
import random

if __name__ =="__main__":
    red = [1]*6 
    i = 0 
    # 隨即產生6個紅色球號碼
    while i<6:
        temp = random.randint(1,33)
        j  =0 
        while j<i:
            # 判断已生成的红色球号码是否与当前while循环中产生的随机红色球号码相同
            # 如果相同，则重新生成新的红色球号码，否则在red[i]中保存新生成的红色球号码
            if red[j] == temp:
                break
            j += 1
        if j==i:
            red[i] = temp 
            i += 1
    # 隨即產生藍色球號碼
    blue = random.randint(1,16)
    print("本期的开奖号码是:") 
    print("红色球:", end=" ") 
    for i in range(6):
        print("%d" % red[i], end=" ") 
        print(" 蓝色球:%d" % blue)
