class Solution(object):
    def isTriangle(self,num_lst):

        if num_lst[0]+num_lst[1]>num_lst[2]:
            return True
        return  False
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        最短两边相加大于第三边
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
                    if self.isTriangle([nums[i], nums[j], nums[z]]):
                        ans.append([nums[i], nums[j], nums[z]])

        # print(sum(nums))
        print(sum(ans[0]))

    def largestPerimeter_leetcode_version(self,nums):
        nums.sort()
        ans = None
        print(nums)
        for i in range(len(nums)-3,-1,-1):

            print(nums[i])
            if nums[i]+nums[i+1]>nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0

nums = [2,1,2]
# nums = [1,2,1,10]
# nums = [3,2,3,4]
nums = [3,6,2,3]


obj = Solution().largestPerimeter_v2(nums)