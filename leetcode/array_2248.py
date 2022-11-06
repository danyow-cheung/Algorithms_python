import collections


class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        多个数组求交集，按照升序排列返回一个数组
        """

        counts = collections.Counter(nums[0])

        for i in nums[1:]:
            counts &= collections.Counter(i)

        res = list(counts.elements())
        res.sort()
        print(res)

nums =[[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
nums =[[7,34,45,10,12,27,13],[27,21,45,10,12,13]]

obj = Solution().intersection(nums)