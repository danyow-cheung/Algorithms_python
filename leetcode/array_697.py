from collections import Counter
from operator import le

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        度指的是數組內任意(要最小的)元素出現的頻次的最大值
        使用左右指針
        """
        # 次数为d的数组必须有某个元素x出现d次。如果某个子数组具有相同的阶数，
        # 那么某个元素x（发生d次）仍然出现d次。最短的子数组将从第一次出现x到最后一次出现
         
        # 使用哈希表存儲，key是元素 value是數值
        res={}
        start = {}
        end ={}

        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]]=1 
                start[nums[i]]=i
                end[nums[i]]=i
            else:
                res[nums[i]]+= 1
                end[nums[i]]=i 

        maxRes = max(res.values())
        lowSpan = len(nums)

        for i in set(nums):
            if res[i]==maxRes:
                span = end[i] - start[i]+1 
                if span < lowSpan:
                    lowSpan = span 
        return lowSpan

nums = [1,2,2,3,1]
nums = [1,2,2,3,1,4,2]
# nums = [0]
# nums = [1,2,1]
obj = Solution().findShortestSubArray(nums)