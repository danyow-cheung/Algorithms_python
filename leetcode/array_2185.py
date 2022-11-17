class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        res = 0
        n = len(pref)
        for i in words:
            if i[:n] == pref:
                res += 1
        return res


words = ["pay","attention","practice","attend"]
pref = "at"
words = ["leetcode","win","loops","success"]
pref = "code"

obj = Solution().prefixCount(words,pref)