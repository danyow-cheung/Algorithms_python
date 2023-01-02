class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ans = len(word)
        print(ans)
        for i in word:
            if i.isupper():
                ans-=1
        # print(ans,word[0])
        if ans==0:
            return True
        elif ans +1 ==len(word) and word[0].isupper():
            return True
        elif ans == len(word):
            return True

        return False

word ='USA'
word = 'FlaG'
obj = Solution().detectCapitalUse(word)