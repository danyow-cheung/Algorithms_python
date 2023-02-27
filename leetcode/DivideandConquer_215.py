class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        print(nums[-k])
        return nums[-k]
        

nums = [3,2,1,5,6,4]
k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 4
obj = Solution().findKthLargest(nums,k)