class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 
        for i in range(len(s)):
            if s[i]=='0':
                return 0 
            for j in range(i+1,len(s)):
                print(s[i:j+1])
                res +=1 
        print(res)

    def numDecodings_leetcode(self, s):
        '''https://leetcode.com/problems/decode-ways/solutions/2645738/python-dp-solutoin-98-fast-space-optimised/
        '''
        dp = [0 for _ in range(len(s)+1)]
        if int(s[0])>0:
            dp[0]= 1 
            dp[1] =1 
        for i in range(2,len(s)+1):

            if int(s[i-1])>0:
                dp[i] =dp[i-1]
            x = s[i-2:i]
            if 10<= int(x)<=26:
                dp[i]+=dp[i-2]
        return dp[len(s)]




s = "12"
s = '226'
s = '06'
obj = Solution().numDecodings(s)
