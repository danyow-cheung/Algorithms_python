from asyncio import FastChildWatcher


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left = 0 
        right = len(s)-1 
        while left<right:
            # 判断顺序的不同
            if not s[left].isalpha() :
                left +=1 
            elif not s[right].isalpha():
                right -= 1 
            else:
                s[left],s[right] =s[right],s[left]
                left+=1 
                right-=1
            
            
        return "".join(s)

        # the same 
        # s, i, j = list(s), 0, len(s) - 1
        # while i < j:
        #     if not s[i].isalpha():
        #         i += 1
        #     elif not s[j].isalpha():
        #         j -= 1
        #     else:
        #         s[i], s[j] = s[j], s[i]
        #         i, j = i + 1, j - 1
        # return "".join(s)
        
    def swap(self,i,j):
        # 交换i，j的数值
        # print(f"i = {i},j={j}")
        temp = i 
        i = j 
        j = temp 
        # print(f"i = {i},j={j}")
        return i,j 

    def reverseOnlyLetters_leetcode_solution_stack(self,s):
        letters = [c for c in s if c.isalpha()]
        print(letters)
        ans = []

        for c in s:
            if c.isalpha():
                # 使用栈的话就是【后进先出】实现反转效果
                ans.append(letters.pop())
            else:
                # 不是字母的话就直接添加
                ans.append(c)
        print(ans)
        return "".join(ans)    

    def reverseOnlyLetters_leetcode_solution_pointer(self,s):
        ans = []
        j = len(s)-1 
        for i,x in enumerate(s):
            if x.isalpha():
                while not s[j].isalpha():
                    j -=1
                # 直接添加后面的字母
                ans.append(s[j])
                j-=1 

            else:
                ans.append(x)
        return "".join(ans)
    
s = 'ab-cd'
i = 10
j = 21
obj = Solution().reverseOnlyLetters_leetcode_solution_pointer(s)
# obj = Solution().swap(i,j)