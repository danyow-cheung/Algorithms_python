class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_word_len = 0
        for i in sentences:
            i = i.split()
            print(i,len(i))
            max_word_len = max(max_word_len,len(i))
        print(max_word_len)
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
sentences = ["please wait", "continue to fight", "continue to win"]
obj = Solution().mostWordsFound(sentences)