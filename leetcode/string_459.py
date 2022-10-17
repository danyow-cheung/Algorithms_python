class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # sub = ""
        # for i in range(len(s)):
        #     # 匹配模式子串(不同元素所以不行)
        #     if s[i] not in sub:
        #         sub+=s[i]
        # print(sub)

        # count = len(s)//len(sub)
        # if (sub*count)==s:
        #     return True 
        # return False 

        return s in s[1:]+s[:-1]
        
    
       
s = "abab"  
# s ="aaaa"
s = "abcabcabcabc"
s = "abaababaab"
obj = Solution().repeatedSubstringPattern(s)
