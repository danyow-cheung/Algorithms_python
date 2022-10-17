import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n  = len(nums)//2
        # for num in nums:
        #     count = sum(1 for elem in nums if elem == num)
        #     if count > n:
        #         return num
        counts = collections.Counter(nums)
        print(counts)
        return max(counts.keys(),key = counts.get)
nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
obj = Solution().majorityElement(nums)

