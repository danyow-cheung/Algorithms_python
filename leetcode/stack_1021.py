import collections


class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        opened = 0
        for c in s:
            print(c,opened)
            if c=='(' and opened>0:
                res.append(c)
            if c==')' and opened>1:
                res.append(c)
            if c=='(':
                opened+=1
            else:
                opened -= 1
        print(res)
        return "".join(res)






s = "(()())(())"
s = "(()())(())(()(()))"

obj = Solution().removeOuterParentheses(s)