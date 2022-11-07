class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []

        i = 0
        j = 0
        while i<len(nums) and j<len(index):

            target.insert(index[j],nums[i])
            i+=1
            j+=1
        print(target)
nums = [0,1,2,3,4]
index = [0,1,2,2,1]

nums = [1,2,3,4,0]
index = [0,1,2,3,0]
nums=[1]
index=[0]
obj = Solution().createTargetArray(nums,index)