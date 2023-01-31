class Solution(object):
    def sortedSquares_brute_force(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] *= nums[i]
        return sorted(nums)

    def sortedSquares_two_pointer(self, nums):
        n = len(nums)
        i = 0 
        j = n-1 
        k = n-1 
        ans = [-1]*n 
        while i<=j:
            lm = nums[i]**2 
            rm = nums[j]**2 
            if lm>rm:
                ans[k]=lm
                i+=1
            else:
                ans[k]=rm
                j-=1 
            k-=1 
        return ans 


        

nums = [-4,-1,0,3,10]
obj = Solution().sortedSquares(nums)