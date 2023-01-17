import collections


class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        https://leetcode.com/problems/flip-string-to-monotone-increasing/solutions/2912351/flip-string-to-monotone-increasing/
        我們枚舉每一個左右窗口配置，使字符串單調遞增的翻轉次數為左窗口'1'的個數和右窗口'0'的個數之和。保存最小值。


        """
        m = 0
        for c in s:
            if c=='0':
                m +=1
        ans = m
        for c in s:
            if c=='0':
                m-= 1
                ans = min(ans,m)
            else:
                m+=1

        return  ans


s = '00110'
obj = Solution().minFlipsMonoIncr(s)