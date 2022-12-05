class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        amount.sort()
        ans = 0
        while sum(amount)!=0:
            amount[2]-=1
            if amount[1]!=0:
                amount[1]-=1
            ans+=1
            amount.sort()
        return  ans



amount= [1,4,2]
obj = Solution().fillCups(amount)