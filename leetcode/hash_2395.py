import collections


class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        see = set()
        for i in range(len(nums)-1):
            # print(nums[i],nums[i+1])
            # print('see=',see)
            first = nums[i]
            second = nums[i+1]
            if first + second in see:
                return True
            see.add(first+second)
        return False


nums = [4,2,4]
nums = [1,2,3,4,5]
obj = Solution().findSubarrays(nums)