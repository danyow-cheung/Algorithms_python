class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_val = max(nums)

        flag = 0
        for i in nums:
            if max_val // 2 >= i:
                flag += 1

        if flag+1 == len(nums):
            return nums.index(max_val)
        return -1

nums = [3,6,1,0]
obj = Solution().dominantIndex(nums)