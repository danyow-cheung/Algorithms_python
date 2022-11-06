import collections


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :hint:
        > Count how many times each number appears. If a number appears n times,
        > then n * (n – 1) // 2 good pairs can be made with this number.
        """
        res =0
        counts = collections.Counter(nums)

        for value in counts.values():
            res += value * (value - 1) // 2
        print(res)

nums = [1,2,3,1,1,3]
nums = [1,1,1,1]
obj = Solution().numIdenticalPairs(nums)