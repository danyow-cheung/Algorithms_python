class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [[1]*i for i in range(1,numRows+1)]
        print(dp)
        for i in dp[2:]:
            print(i)
            for j in i:
                pass

numRows = 5
obj = Solution().generate(numRows)