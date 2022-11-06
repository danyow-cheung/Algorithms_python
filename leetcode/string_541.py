class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
        如果剩余字符少于 k 个，则将剩余字符全部反转。
        如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

        """
        for i in range(0,len(s),2*k):

            if (i+k<len(s)):
                s = s[0:i]+s[i:i+k][::-1]+s[i+k:]
            else:
                s = s[0:i]+s[i:i+k][::-1]
        return s
s = "abcdefg"
# s= "abcd"
k = 2
obj = Solution().reverseStr(s,k)