class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left= 0
        right = len(s) -1 
        a_lst =['a','e','i','o','u','A','E','I','O','U']
        s_lst = list(s)
        while left < right:
            if s_lst[left] in a_lst and s_lst[right] in a_lst:
                s_lst[left],s_lst[right]=s_lst[right],s_lst[left]
                left+=1
                right-=1
            elif s_lst[left] in a_lst:
                right -=1 
            elif s_lst[right] in a_lst:
                left +=1
            # 不加这一步就超时
            
            else:
                left +=1 
                right -=1 

            
        print("".join(s_lst))



s = "hello"
s = "leetcode"

obj = Solution().reverseVowels(s)




