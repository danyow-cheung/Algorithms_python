class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/solutions/2846330/python-96-67-faster-two-pointers-o-n-solution/
        """
        left = 0
        right = len(s)-1
        while left<right and s[left]==s[right]:
            t = s[left]
            while left<len(s) and s[left]==t:
                left+=1
            while right>=0 and s[right]==t:
                right-=1
        if right<left:
            return 0
        return  right-left+1

s = "ca"
s = "cabaabac"
# s = "aabccabba"

obj = Solution().minimumLength(s)