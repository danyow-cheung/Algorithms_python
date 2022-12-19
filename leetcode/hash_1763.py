import collections


class Solution(object):
    def decide_(self,arr):
        arr = 'aAa'
        for i in arr:
            if i.lower():
                convert = i.upper()
                if convert in arr:
                    return True
            else:
                convert = i.lower()
                if convert in arr:
                    return  True
        return False



    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans =""
        for i in range(len(s)):

            for j in range(i):
                print(s[j:i+1])
                sub = s[j:i+1]
                '''swapcase:將小寫字母變成大寫字母，將大寫字母變成小寫字母'''
                if set(sub)==set(sub.swapcase()):
                    return max(ans,sub,key=len)
        return ans

    def longestNiceSubstring_leetcode(self,s):
        ans = ""
        for j in range(len(s)):
            for i in range(j):
                t = s[i: j + 1]
                if set(t) == set(t.swapcase()):
                    ans = max(ans, t, key=len)
        return ans
s = 'YazaAay'
obj = Solution().longestNiceSubstring(s)