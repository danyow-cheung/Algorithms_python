import collections


class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = collections.Counter(s)
        print(count)
        ans = []
        for i in count.values():
            ans.append(i)

        for i in range(len(ans) - 1):
            if ans[i] != ans[i + 1]:
                return False
        return True

s = "abacbc"
s = "aaabb"

obj = Solution().areOccurrencesEqual(s)