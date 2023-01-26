class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d= {}
        # index-value 
        for i ,j in enumerate(nums):
            # print(i,j)
            r = target - j 
            if r in d:
                return[d[r],i]
            d[j]=i 
        

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 9

obj = Solution().twoSum(nums,target)