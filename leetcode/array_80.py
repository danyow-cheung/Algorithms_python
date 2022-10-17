class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 雙指針---通過測試
        j = 0
        for i in range(1,len(nums)):
            if nums[j]!=nums[i]:
                j += 2
                nums[j] = nums[i]
        return j+1 

nums= [1,1,2]

obj = Solution().removeDuplicates(nums)