class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        left =0
        right = left+n
        while left<len(nums):
            res.append(nums[left])
            if right<len(nums):
                res.append(nums[right])
                right+=1
            if len(nums)-left-1==n:
                break
            left+=1
        print(res)
nums = [2,5,1,3,4,7]
n = 3
obj = Solution().shuffle(nums,n)