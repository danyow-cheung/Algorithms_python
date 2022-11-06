class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res_2=[]
        for i in nums:
            res_2.append(nums[i])
            # print(nums[i])
        # print(res_2)
        return res_2

nums = [0,2,1,5,3,4]
nums = [5,0,1,2,3,4]
obj = Solution().buildArray(nums)