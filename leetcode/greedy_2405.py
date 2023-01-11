import collections


class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = []
        s = list(s)
        i = 0

        left= 1
        print(s[0:1])
        # exit(0)
        while i <len(s):
            if s[i] != s[left] :
                left +=1

            elif s[i]==s[left]:
                # seen.append(s[i:left])
                print(s[i:left])
                i = left
            else:
                i+=1

    def partitionString_leetcode(self,s):

        e = ""
        g = []
        for i in range(len(s)):
            if s[i] not in e:
                e = e+s[i]
            else:
                g.append(e)
                e = ""
                e = e+s[i]
        print(e,g)

        return len(g)+1

s = "abacaba"
# s = "hdklqkcssgxlvehva"
obj = Solution().partitionString_leetcode(s)