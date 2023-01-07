class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        ans = 0
        for i in costs:
            if i <= coins:
                ans += 1
                coins -= i
            if coins == 0:
                break
        return ans

costs = [1,3,2,4,1]
coins = 7
obj = Solution().maxIceCream(costs,coins)