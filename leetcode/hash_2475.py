class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if set(nums)==1:
            return 0
        nums.sort()
        print(nums)
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for z in range(j+1,len(nums)):
                    if nums[i]!= nums[j] and nums[j]!= nums[z] and nums[i]!= nums[z]:

                        print(nums[i],nums[j],nums[z])
                        ans +=1

        print(ans)
        return  ans


nums =[4,4,2,4,3]
nums = [1,1,1,1,1]
obj = Solution().unequalTriplets(nums)