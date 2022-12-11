class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        ans = 0
        for i in range(len(nums)):
            ans += (0^nums[i])
            cur = 0
            for j in range(i+1,len(nums)):
                # print(nums[i:j+1])
                cur ^= nums[i:j+1]
                ans+=cur


        print(ans)
        if len(nums)>2:
            cur = 0
            for i in nums:
                cur ^= i
            ans+=cur
        print(ans)
        return ans

nums = [1,3]
nums =[5,1,6 ]
nums = [3,4,5,6,7,8]
obj = Solution().subsetXORSum(nums)
