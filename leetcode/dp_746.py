class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)+1
        dp =[0]*n
        # 默認第一步都是不花力氣的
        dp[0]=0
        dp[1]=0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[len(cost)]

    def minCostClimbingStairs_leetcode(self, cost):
        '''
        https://leetcode.com/problems/min-cost-climbing-stairs/solutions/3021926/python-dynamic-programming-4-lines-of-code/
        '''
        c1 = cost[0]
        c2 = cost[1]
        for i in range(2,len(cost)):
            c1,c2 = c2,min(c1,c2)+cost[i]
        return min(c1,c2)
