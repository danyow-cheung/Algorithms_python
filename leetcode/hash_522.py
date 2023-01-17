import collections


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        c = collections.Counter(strs)
        def isSub(s1,s2):
            it = iter(s2)
            return all(i in it for i in s1)
        for s1 in sorted([str for str in c if c[str] == 1], key=len, reverse=True):
            if sum(isSub(s1,s2) for s2 in strs)==1:
                return len(s1)
        return -1


strs = ["aba","cdc","eae"]
obj = Solution().findLUSlength(strs)