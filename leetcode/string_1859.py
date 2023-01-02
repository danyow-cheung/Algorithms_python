class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        output =""
        sarray = s.split()

        for i in range(1,10):
            for word in sarray:
                if word[-1]==str(i):
                    output+=" "+word[:-1]
        return output.strip()

s = "is2 sentence4 This1 a3"
obj = Solution().sortSentence(s)