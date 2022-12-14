import collections


class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """

        count1 = collections.Counter(target)
        count2=collections.Counter(arr)
        print(count1==count2)
        # return set(target)==set(arr)
target = [1,2,3,4]
arr = [2,4,1,3]
arr = [1,1,2,3]


obj = Solution().canBeEqual(target,arr)