class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        print(nums[-1])
        print(nums[-2])
        return (nums[-1]-1)*(nums[-2]-1)
nums = [3,4,5,2]
obj = Solution().maxProduct(nums)