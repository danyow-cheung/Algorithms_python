class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x<0:
            negative = True
        else:
            negative = False
        
        if negative:
            # # print()
            print(int(str(x[1:])[::-1]))
        else:
            print(int(str(x)[::-1]))

x = 123
x = -123
# x = 120
obj = Solution().reverse(x)