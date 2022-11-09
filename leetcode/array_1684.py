class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        给你一个由不同字符组成的字符串allowed和一个字符串数组words。
        如果一个字符串的每一个字符都在 allowed中，就称这个字符串是 一致字符串 。
        请你返回words数组中一致字符串 的数目。
        """
        res = 0
        for i in range(len(words)):
            if words[i] in allowed:
                print(words[i])
                res +=1
        print(res)

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

# allowed = "abc"
# words = ["a","b","c","ab","ac","bc","abc"]
obj = Solution().countConsistentStrings(allowed,words)