import collections
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        # # for i in range(len(nums)-1):
        # while i<len(nums):
        #     if nums[i]==nums[i+1]:
        #         i+=2 
            
        #     i+=1 

        count = collections.Counter(nums)
        res = None
        for i in count.keys():
            if count[i]==1:
                res = i
        print(res)



nums = [1,1,2,3,3,4,4,8,8]
nums = [3,3,7,7,10,11,11]

obj =Solution().singleNonDuplicate(nums)