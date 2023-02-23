class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0 

        for i in range(len(s)-1):
            # print(s[i])
            if rti[s[i]] <rti[s[i+1]]:
                ans = ans - rti[s[i]]
            else:
                ans = ans + rti[s[i]]
        
        return ans +rti[s[-1]]


s = "III"
obj = Solution().romanToInt(s)
