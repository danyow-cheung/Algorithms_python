from asyncio import FastChildWatcher


class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag_small = True
        flag_big = True 
        
        for i in nums:
            if i <i+1:

                flag_small = False
            if i>i+1:
                
                flag_big = False
      
        return flag_small or flag_big

    def isMonotonic_leetcode(self,nums):
        increasing = decreasing = True 
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                increasing = False 
            if nums[i]<nums[i+1]:
                decreasing = False 
        return increasing or decreasing
       
nums = [1,2,2,3]
obj = Solution().isMonotonic_leetcode(nums)