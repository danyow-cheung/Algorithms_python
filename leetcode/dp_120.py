class Solution(object):
    def minimumTotal_recursion(self, triangle):
        '''回溯方法
        https://leetcode.com/problems/triangle/solutions/2146264/c-python-simple-solution-w-explanation-recursion-dp/
        '''
        def dfs(i,j):
            if i==len(triangle):
                return 0 
            lower_left = triangle[i][j] +dfs(i+1,j)
            lower_right = triangle[i][j]+dfs(i+1,j+1)
            return min(lower_left,lower_right)

        return dfs(0,0)
    def minimumTotal_dp(self, triangle):
        memo = [[-1]*len(triangle) for _ in range(len(triangle))]
        def dfs(i,j):
            if i==len(triangle):
                return 0 
            if memo[i][j]!=-1:
                return memo[i][j]
            lower_left = triangle[i][j] + dfs(i+1,j)
            lower_right = triangle[i][j] + dfs(i+1,j+1)
            memo[i][j] = min(lower_left,lower_right)
            return memo[i][j]

        return dfs(0,0)
        

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        找出自顶向下的最小路径和。
        """
        # dp = [[-1] for i in range(len(triangle))]
        # print(dp)
        res = 0

        for i in range(len(triangle)):
            res += min(triangle[i])
            # if abs(res):
        print(res)
        return res 


        

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
triangle = [[-1],[2,3],[1,-1,-3]]


obj = Solution().minimumTotal(triangle)