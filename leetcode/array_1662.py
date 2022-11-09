class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        string_1 = "".join(word1)
        print(string_1)
        return "".join(word1)=="".join(word2)


word1 = ['ab','c']
word2 = ['a','bc']
obj = Solution().arrayStringsAreEqual(word1,word2)