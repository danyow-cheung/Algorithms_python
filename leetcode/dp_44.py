class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        這誰會我反正不會
        """
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1,len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] in {s[i-1],'?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
        


s = "aa"
p = "a"
obj = Solution().isMatch(s,p)