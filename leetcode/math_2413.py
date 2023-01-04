class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        给一个正整数，返回2和n的最小公倍数
        """
        if n%2==0:
            return  n
        return  2*n


n = 5
obj = Solution().smallestEvenMultiple(n)