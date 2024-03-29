class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 初始化dp數組
        # [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        dp = [[0 for i in range(n)] for j in range(m)]
        # print(dp)
        for  i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
                
        print(dp)
        return dp[m-1][n-1]