class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(heights)):
            while heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i-stack[-1]-1
                ans = max(ans,h*w)
            stack.append(i)
        heights.pop()
        return ans 
        


heights = [2,1,5,6,2,3]
obj = Solution().largestRectangleArea(heights)