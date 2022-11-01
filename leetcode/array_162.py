class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0 
        right = len(nums)-1 
        while left<right:
            mi = (left+right)//2 
            
            if nums[mi]<nums[mi+1]:
                left=mi+1 
            else:
                right = mi
        
        return left

nums = [1,2,3,1]
nums = [1,2,1,3,6,4]
obj = Solution().findPeakElement(nums)