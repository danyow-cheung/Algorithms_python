class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        TLE:brute loop
        """
        ans = 0
        for i in range(len(prices)-1):
            print(prices[i],prices[i+1:])
            max_val = max(prices[i+1:])
            if max_val<prices[i]:
                continue
            else:
                ans = max(max_val-prices[i],ans)
        print(ans)
        return ans
    def maxProfit_v2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        two pointer
        """
        left = 0# buy socks
        right = 1 # sell socks
        max_profix = 0
        while right<len(prices):
            curr = prices[right]-prices[left] # curr profit
            # 如果buy的值比sell高，profix保持为0
            if prices[left]<prices[right]:
                max_profix = max(curr,max_profix)
            else:
                left = right
            right +=  1
        return  max_profix



prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]


obj = Solution().maxProfit(prices)