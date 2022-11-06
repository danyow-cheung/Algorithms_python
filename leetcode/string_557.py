class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        res = []
        for i in s:
            res.append(i[::-1])
        print(" ".join(res))


        #print(" ".join(res))
s = "Let's take LeetCode contest"
s = "God Ding"
obj = Solution().reverseWords(s)