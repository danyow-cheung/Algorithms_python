class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        # 分為n組對
        n = len(nums)//2

        left = 0
        max_lst = []
        print(nums)

        for i in range(0,len(nums),2):
            max_lst.append(min(nums[i],nums[i+1]))

        print(max_lst)
        return sum(max_lst)
nums = [1,4,3,2]
# nums = [6,2,6,5,1,2]
obj = Solution().arrayPairSum(nums)