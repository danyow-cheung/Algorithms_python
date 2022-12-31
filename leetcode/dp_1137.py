class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0, 1, 1]

        if n < 3:
            return dp[n]

        for i in range(3, n + 1):
            # print(i)
            dp.append(dp[-1] + dp[-2] + dp[-3])

        return dp[n]

n = 4
obj = Solution().tribonacci(n)