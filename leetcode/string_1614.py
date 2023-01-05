import collections


class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = collections.deque()
        ans = 0
        for i in s:
            if i =="(":
                stack.append(i)
            elif i==")":
                stack.popleft()
            diff = len(stack)
            ans = max(diff,ans)
        print(stack)
        if len(stack)==0:
            print("ans",ans)


s = "(1+(2*3)+((8)/4))+1"
s = "(1)+((2))+(((3)))"
obj = Solution().maxDepth(s)