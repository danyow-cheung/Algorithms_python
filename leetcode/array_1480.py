class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res= []
        for i in range(len(nums)):
            # print(nums[:i+1])
            max = 0
            for j in nums[:i+1]:
                max +=j
            res.append(max)
        print(res)


nums = [1,2,3,4]
nums =[1,1,1,1,1]
obj = Solution().runningSum(nums)