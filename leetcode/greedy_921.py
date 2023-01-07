class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        s = list(s)
        print('s=',s)
        for i in range(len(s)):
            print('stack=',stack)
            if s[i]=="(":
                stack.append(s[i])
            # 如果当前栈没有元素，则加入
            # elif len(stack)==0:
                # stack.append(s[i])
            # 碰到），弹出对应的（
            elif "(" in stack and s[i]==')':
                stack.pop()
            else:
                stack.append(s[i])

        print(stack)

        print(max(stack.count("("), stack.count(")")))
        if "(" not in stack:

            return stack.count(")")
        elif ")" not in stack:
            return stack.count("(")
        else:
            return len(stack)


s = '())'
# s = "((("

s = "()))(("

obj = Solution().minAddToMakeValid(s)