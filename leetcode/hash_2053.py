import collections


class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = collections.Counter(arr)
        for i in arr:
            if count[i] == 1: k -= 1
            if k == 0: return i
        return ""
arr = ["d","b","c","b","c","a"]
k = 2
obj = Solution().kthDistinct(arr,k)