class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")

        for word in words:
            w = set(word.lower())
            if w<= first or w<= second or w<= third:
                ans.append(word)
        print(ans,type(ans))

        return  ans
words = ["Hello", "Alaska", "Dad", "Peace"]
obj =Solution().findWords(words)