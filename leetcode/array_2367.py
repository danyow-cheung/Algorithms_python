class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        算术三元组的数目
        """
        res = 0
        for i in range(len(nums)):
            for  j in range(i,len(nums)):
                for z in range(j,len(nums)):
                    if nums[j]-nums[i]==diff and nums[z]-nums[j]==diff:
                        res +=1
        print(res)
    def arithmeticTriplets_leetcode(self,nums,diff):
        ans = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i]+diff in nums and nums[i]+2*diff in nums:
                ans +=1
        return ans

nums = [0,1,4,6,7,10]
diff =3
obj = Solution().arithmeticTriplets(nums,diff)