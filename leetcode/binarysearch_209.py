class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        res = float('inf')
        # 滑動窗口數值之和
        Sum = 0 
        # 滑動窗口起始位置
        i = 0 
        for j in range(len(nums)):
            Sum += nums[j]
            while Sum>=target:
                res = min(res,j-i+1)
                Sum -= nums[i]
                i+=1 
            return 0 if res==float('inf')else res 
            



target = 7
nums = [2,3,1,2,4,3]
obj = Solution().minSubArrayLen(target,nums)