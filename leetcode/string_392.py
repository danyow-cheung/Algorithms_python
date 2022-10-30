class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        right = 0

        # 对应字母,存储下标
        res = []
        n = len(t)
       
        #while right<len(t):
        while right<n:
            # 更新下标操作
            if t[right] in s :
                res.append(right)        
            right+=1

        print(res)
        print("".join(t[i] for i in res) == s)
    
    def isSubsequence_leetcode(self,s,t):
        i,j = 0,0 
        while i <len(s) and j<len(t):
            if s[i]==s[j]:
                i+=1
            j+=1
        return i==len(s)
        
        
s  = "abc"
t  = "ahbgdc"
s = "axc"
t = "ahbgdc"
s = 'ab'
t='baab'
obj = Solution().isSubsequence(s,t)