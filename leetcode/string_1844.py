class Solution(object):

    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def shift(alpha,num):
            print(ord(alpha),ord(alpha)+num)

        for i in range(len(s)):
            if i % 2 == 0:
                continue
            else:
                s[i] = shift(s[i - 1], int(s[i]))
        print(s)
s = "a1c1e1"
obj = Solution().replaceDigits(s)