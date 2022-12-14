class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text_af = text.split()
        print('text_af=',text_af)
        ans = 0

        for i in range(len(text_af)):
            print(text_af[i])
            len_word = len(text_af[i])
            cur = len_word
            for j in text_af[i]:
                if j in brokenLetters:
                    cur -=1
            # print('cur=',cur)
            if cur==len_word:
                ans+=1
        print(ans)
        return  ans


text = "hello world"
brokenLetters = "ad"
obj = Solution().canBeTypedWords(text,brokenLetters)