class Solution(object):
    def isMatch(self, text, pattern):
        '''
        https://leetcode.com/problems/regular-expression-matching/solutions/127565/regular-expression-matching/
        超時
        '''
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

class Solution(object):
    def isMatch_recursion(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        https://leetcode.com/problems/regular-expression-matching/solutions/127565/regular-expression-matching/

        """
        if len(p)<len(s):
            return False
        first_match = bool(s) and p[0] in {s[0],'.'}
        if len(p)>=2 and p[1]=='*':
            return (self.isMatch_recursion(s,p[2:]) or first_match and self.isMatch_recursion(s[1:],p))
        else:
            return first_match and self.isMatch_recursion(s[1:],p[1:])
        
    def isMatch_dp(self, s, p):
        memo = {}
        def dp(i,j):
            if (i,j) not in memo:
                if j==len(p):
                    ans = i ==len(s)
                else:
                    first_match = i<len(s) and p[i] in {s[i],'.'}
                    if j+1<len(p) and p[j+1]=='*':
                        ans = dp(i,j+2) or first_match and dp(i+1,j)
                    else:
                        ans = first_match and dp(i+1,j+1)
                memo[i,j]=ans 
            return memo[i,j]
        return dp(0,0)
        
        

    

s = "aa"
p = "a"
obj = Solution().isMatch(s,p)
