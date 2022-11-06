import collections


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cur = sorted(nums)
        print(cur,nums)
        print([cur.index(i) for i in nums])
        '''
        cur:    [1, 2, 2, 3, 8] 
        nums:   [8, 1, 2, 2, 3]
        return: [4, 0, 1, 1, 3]
        '''



nums = [8,1,2,2,3]
obj = Solution().smallerNumbersThanCurrent(nums)