class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cur = 0
        for i in range(len(nums)):

            if i + nums[i] >= 1  :
                print(i,cur)
                cur+= i+ nums[i]
                ans = min(ans,cur)
        # print(ans)

nums = [-3,2,-3,4,2]
obj =Solution().minStartValue(nums)