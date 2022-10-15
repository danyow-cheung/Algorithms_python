class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        找到出现两次的数字和缺少的数字，并以数组的形式返回它们
        """

        sum_nums = sum(nums)
        set_nums  = sum(set(nums))
        dup = sum_nums - set_nums
         
        nums_copy = set(range(1,len(nums)+1))

        diff=list(set(nums_copy).difference(set(nums)))
        diff.insert(0,dup)
        return diff 

    
nums= [1,2,2,4]
# nums = [2,2]
nums= [1,1]
# obj = Solution().findErrorNums_leetcode_example(nums)
obj = Solution().findErrorNums(nums)