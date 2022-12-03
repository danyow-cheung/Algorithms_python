class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return  0

        # 需要在原數組上進行操作
        res= 0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                diff = nums[i]-nums[i+1]+1
                nums[i+1] += diff
                res+=diff


            # else:
            #     # print(nums[i])
            #     for j in range(i,len(nums)):
            #         print(j,nums[j],nums[i])
            #         nums[j]+=1

            # res+=1
        print(res)
        print(nums)

# nums = [1,1,1]
nums = [1,5,2,4,1]
obj = Solution().minOperations(nums)