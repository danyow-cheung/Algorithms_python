class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0]*(n+2)
        nums[1] = 1
        for i in range(2,n+1):
            nums[i] = nums[i//2]+nums[(i//2)+1]*(i%2)
        print(nums)
        return max(nums[:n+1])


n = 7
obj = Solution().getMaximumGenerated(n)