class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        type = heights[:]
        heights.sort()
        print(type,heights)
        for i in range(len(type)):
            if type[i]!= heights[i]:
                ans +=1
        print(ans)

heights = [1,1,4,2,1,3]
obj = Solution().heightChecker(heights)