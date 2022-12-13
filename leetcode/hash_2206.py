import collections


class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)//2
        print('n=',n)
        nums.sort()
        print(nums)
        for i in range(0,len(nums),2):
            print(nums[i], nums[i + 1])
            if nums[i]!=nums[i+1]:

                return False
        return True


nums = [3,2,3,2,2,2]
# nums =[1,2,3,4]
obj = Solution().divideArray(nums)