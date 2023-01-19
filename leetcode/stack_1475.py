class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                print(prices[i],prices[j])
                if prices[j]<=prices[i]:
                    ans.append(prices[i]-prices[j])
                    break
        print(ans)
        if len(ans)<len(prices):
            for i in prices[len(ans):]:
                ans.append(i)
            # ans.append(i for i in prices[len(ans):])
            # ans.

        print(ans)
        return  ans

    def finalPrices_leetcode(self, prices):
        '''stack,one pass'''
        stack = []
        for i,a in enumerate(prices):
            while stack and prices[stack[-1]]>=a:
                prices[stack.pop()]-=a
            stack.append(i)
        return  prices

prices = [8,4,6,2,3]
# prices = [1,2,3,4,5]
prices = [10,1,1,6]

obj = Solution().finalPrices(prices)