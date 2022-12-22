import collections


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        countS = collections.Counter(s)
        countT = collections.Counter(t)
        print(countS,countT)
        for key in countT.keys():
            if key not in countS:
                print(key)
                return key
            elif countT[key]!=countS[key]:
                print(key)
                return key
s = 'abcd'
t = 'abcde'

s =""
t= 'y'

s ="a"
t= 'aa'

obj = Solution().findTheDifference(s,t)