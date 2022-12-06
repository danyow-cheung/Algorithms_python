class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        两边相加大于第三边
        返回三条边的累加
        最大值加最小值<中间值或第二个大的值
        https://leetcode.com/problems/largest-perimeter-triangle/
        """
        ans = []
        nums.sort()
        print(nums)
        for i in (range(len(nums))):
            for j in (range(i+1,len(nums))):
                for z in range(j+1,len(nums)):
                    if nums[j]+nums[z]>nums[i]:
                        print(nums[i],nums[j],nums[z])
        # print(sum(nums))


nums = [2,1,2]
nums = [1,2,1,10]
obj = Solution().largestPerimeter(nums)