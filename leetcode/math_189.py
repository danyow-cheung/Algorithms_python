class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        TIME_EXCEED_LIMIT
        """
        for i in range(k):
            # print(i)
            nums.insert(0,nums[-1])
            nums.pop()
        print(nums)
        


nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution().rotate(nums,k)
