import collections


class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)//2
        print(n)
        count = collections.Counter(nums)
        for key,value in count.items():
            if value==n:
                return key
        return 0


nums = [1,2,3,3]
obj =Solution().repeatedNTimes(nums)