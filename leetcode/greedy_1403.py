class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        返回长度最短以及总和最大的子序列
        """
        nums.sort()
        print(nums)
        res = []
        # 倒序输出
        for i in range(1,len(nums)+1):

            res.append(nums[-i])
            print(nums[-i],nums[0:-i])

            if sum(res)>sum(nums[0:-i]):
                break
                return res
        print(res)

nums = [4,3,10,9,8]
nums = [4,4,7,6,7]
obj = Solution().minSubsequence(nums)
