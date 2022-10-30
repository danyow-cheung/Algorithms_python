class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        res = 0 
        for i in patterns:
            if i in word:
                res+=1 
        print(res)
        return res 
        
patterns = ["a","abc","bc","d"]
word = "abc"
patterns = ["a","b","c"]
word = "aaaaabbbbb"
obj = Solution().numOfStrings(patterns,word)