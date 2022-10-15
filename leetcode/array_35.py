class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0 
        high = len(nums) - 1 
        
        while low <= high:
            mid = (low+high)//2 
            if target >nums[mid]:
                low = mid +1 
            elif target<nums[mid]:
                high = mid -1 
            else:
                return mid 
        # 没找到的话返回
        return low 

nums= [1,3,5,6]
target = 2 
obj = Solution().searchInsert(nums,target)