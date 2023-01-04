class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i],nums[left] = nums[left],nums[i]
                left+=1
        print(nums)
        return  nums

nums = [3,1,2,4]
obj = Solution().sortArrayByParity(nums)