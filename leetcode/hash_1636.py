import collections


class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)

        return sorted(nums,key=lambda num:(count[num],num))
            # print(count[i],nums[i])
nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]

obj = Solution().frequencySort(nums)