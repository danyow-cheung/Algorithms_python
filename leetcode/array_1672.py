class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res  = 0
        for i in range(len(accounts)):
            wealth = 0
            # print(i)
            for j in accounts[i]:
                # print(j)
                wealth += j
            res = max(wealth,res)
        print(res)
accounts = [[1,2,3],[3,2,1]]
accounts = [[2,8,7],[7,1,3],[1,9,5]]
obj = Solution().maximumWealth(accounts)