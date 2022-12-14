class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        left = 0
        print(nums,nums[-1])
        ans = 0
        while left<len(nums):
            x = nums[left]
            print(left, x, nums)
            if x==0:
                left+=1
            else:
                for i in range(len(nums)):
                    nums[i]-=x
                ans+=1
        print('ans=',ans)
        return  ans
nums = [1,5,0,3,5]
# nums=[1,1,1,2,2,2,3,3,3]
obj = Solution().minimumOperations(nums)