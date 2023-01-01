class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = []
        left = 0

        while left<len(word1) or left<len(word2):
            if left<len(word1) and left<len(word2):
                ans.append(word1[left])
                ans.append(word2[left])
            elif left<len(word1):
                ans.append(word1[left])
            else:
                ans.append(word2[left])
            left+=1


        print(ans)
        return "".join(ans)


word1 = "abc"
word2 = "pqr"

# 主要问题是长度不一致，如何去平衡长的哪一个
word1 = "ab"
word2 = "pqrs"
obj = Solution().mergeAlternately(word1,word2)