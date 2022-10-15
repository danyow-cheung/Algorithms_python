class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math 
        res = int(math.sqrt(x))
        return res

x = 8
obj = Solution().mySqrt(x)