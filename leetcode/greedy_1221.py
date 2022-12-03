class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        Balanced strings are those that have an equal [quantity] of 'L' and 'R' characters.
        返回你可以獲得的最大平衡字符串數
        return the maximum number of balanced strings you can obtain
        """

        l_count = 0

        res=0

        for i in range(len(s)):

            if s[i]=='L':
                l_count+=1
            elif s[i]=='R':
                l_count -=1

            if l_count==0:
                res+=1

        print(res)
        return res


s = "RLRRLLRLRL"
# s = "RLRRRLLRLL"
obj = Solution().balancedStringSplit(s)
