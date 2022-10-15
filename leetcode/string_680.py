class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        给你一个字符串 s，最多 可以从中删除一个字符。
        请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
        """
        # left = 0 
        # right = len(s)-1 
        # while left < right:
        #     if s[left]==s[right]:
        #         left+=1 
        #         right-=1 
        #     else:
        #         s = s.remove(s[left])
        #         left+=1
        # # 找到回文字符串
        # if left ==right:return True 
        # return False
        
        # 使用到双指针和迭代
        left = 0 
        right = len(s)-1 
        while left<right:
            if s[left]==s[right]:
                left+=1 
                right -=1 
            else:
                return self.loop(s,left+1,right) or self.loop(s,left,right-1 )
        return True 

    def loop(self,s,i,j):
        while i<j:
            if s[i]==s[j]:
                i+=1 
                j-=1 
            else:
                return False  
        return True 

s = "abca" 
obj=  Solution().validPalindrome(s)