class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        print(res)

nums = [1,2,5,2,3]
target = 2
nums = [1,2,5,2,3]
target = 3
obj = Solution().targetIndices(nums,target)