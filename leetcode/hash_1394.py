import collections


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = collections.Counter(arr)
        cur = []
        for key,value in count.items():

            if key==value:
               cur.append(key)
        if cur:
            return max(cur)
        return -1
arr = [2,2,3,4]
obj = Solution().findLucky(arr)