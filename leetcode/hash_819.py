import collections


class Solution(object):

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hash_ = {}

        paragraph = paragraph.lower().split()
        for i in paragraph:

            if i not in hash_:
                hash_[i]=1
            else:
                hash_[i]+=1
        print(hash_)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

obj = Solution().mostCommonWord(paragraph,banned)