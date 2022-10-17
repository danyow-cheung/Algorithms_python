class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        包含数字字母
        """
        # 转换为小写，消除标点符号
        # 1. 使用过滤器
        # 2. 正则表达式
        #s = s.lower()
        #s="".join(filter(str.isalnum, s))
        #print(s,type(s))
        
        # # 双指针
        # left = 0 
        # right = len(s)-1
        # while left<right:
        #     if s[left]==s[right]:
        #         left +=1 
        #         right -=1 
        #     else:
        #         return False
        # return True 
        string = ''
        for i in s:
            if i.isalnum():
                string+=i.lower()
        left = 0
        right = len(string)-1 
        while left<right:
            if string[left]==string[right]:
                left+=1 
                right-=1 
            else:
                return False 
        return True 
        
s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "
s = "a."
s ="ab@a+-./~"
# s = "0P"
obj = Solution().isPalindrome(s)