class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        
        while original in nums:
            original *=2
        print(original)
        return original


nums = [5,3,6,1,12]
original = 3 
nums = [2,7,9]
original = 4

obj = Solution().findFinalValue(nums,original)