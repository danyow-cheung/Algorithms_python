class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)

        while max_val % min_val:
            max_val, min_val = min_val, max_val % min_val
        return min_val


