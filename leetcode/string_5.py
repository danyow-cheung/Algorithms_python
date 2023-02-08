class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                print(s[i:j+1])
                
                if s[i:j+1]==s[i:j+1][::-1]:
                    print(s[i:j+1])
                    return s[i:j+1]
        

s = "babad"
obj = Solution().longestPalindrome(s)