class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数
        """
        res = 0
        for i in nums:

            if len(str(i)) %2==0:
                print(i)
                res+=1

        return res

nums = [555,901,482,1771]
nums = [12,345,2,6,7896]
obj = Solution().findNumbers(nums)