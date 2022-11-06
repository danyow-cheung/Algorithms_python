import copy


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =copy.copy(nums)
        print(res+nums)
nums = [1,2,1]
# nums=[1,3,2,1]
obj = Solution().getConcatenation(nums)