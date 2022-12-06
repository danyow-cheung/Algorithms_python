class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        while i < len(s):
            if s[i] == "X":
                i += 3
                res += 1
            else:
                i += 1

        return res



s = "XXX"
s = 'XXOX'
s = "OXOX"
obj = Solution().minimumMoves(s)