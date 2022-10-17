class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(1,len(nums)+1):
            
            if i not in set(nums):
                # 損耗資源
                res.append(i)
        return res
        '''下面的work'''
        _set = set(nums)
        return [i for i in range(1,len(nums)+1) if i not in _set]
        


nums = [4,3,2,7,8,2,3,1]
# nums= [1,1]
obj = Solution().findDisappearedNumbers(nums)
