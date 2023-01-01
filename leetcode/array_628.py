class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        v1 = nums[0] * nums[1] * nums[2]
        v2 = nums[0] * nums[-1] * nums[-2]
        return max(v1, v2)

nums =[-100,-98,-1,2,3,4]
obj = Solution().maximumProduct(nums)