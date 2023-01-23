class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] *= nums[i]
        return sorted(nums)
        

nums = [-4,-1,0,3,10]
obj = Solution().sortedSquares(nums)