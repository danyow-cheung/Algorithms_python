class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        t = self.grayCode(n-1)
        return t+[i+(1<<(n-1)) for i in t][::-1]

n = 2
obj = Solution().grayCode(n)
