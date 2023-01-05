class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        print(piles)

        ans = 0
        itr = 0
        l = len(piles)-2
        while l>=0 and itr<len(piles)//3:
            ans += piles[l]
            print('ans,piles[l]=',ans,piles[l])
            l-=2 # update
            itr+=1
        return  ans

    def maxCoins_v2(self, piles):
        # ref:https://leetcode.com/problems/maximum-number-of-coins-you-can-get/solutions/2857998/python3-easy-fast-and-efficient-way/
        ans = 0
        piles.sort()
        for ii in range(len(piles)//3):
            ans += piles[-2-2*ii]
        return  ans

piles = [2,4,1,2,7,8]
piles = [2,4,5]
piles = [9,8,7,6,5,1,2,3,4]

obj = Solution().maxCoins_v2(piles)