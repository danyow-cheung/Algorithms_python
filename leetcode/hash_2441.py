class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        # left = 0
        right = len(nums)-1

        ans= 0
        while True:
            if right==0:
                ans = -1
                break
            if -nums[right] in nums:
                ans=nums[right]
                break
            right-=1

        print(ans)
        return  ans

nums = [-1,2,-3,3]
nums = [-1,10,6,7,-7,1]
nums = [-10,8,6,7,-2,-3]
obj = Solution().findMaxK(nums)