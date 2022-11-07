class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res =[]
        print(max(candies))
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        print(res)
candies = [2,3,5,1,3]
extraCandies = 3
candies = [4,2,1,1,2]
extraCandies = 1
obj = Solution().kidsWithCandies(candies,extraCandies)