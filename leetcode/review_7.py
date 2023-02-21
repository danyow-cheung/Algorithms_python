class Solution:
    def reverse(self, x):
        
        flag = 0
        if x<0:
            flag = 1
            x = abs(x)
            
        y = str(x)[::-1]
        if flag == 1:
            y = '-' + y
        print(y)
        # 自动去0
        y = int(y)
        # 上下界
        if y<-(2**31) or y>=(2**31):
            return 0
        else:
            print(y)
            return y

        
x = 901000

obj = Solution().reverse(x=x)           

x = 123
x = -123
# x = 120
obj = Solution().reverse(x)