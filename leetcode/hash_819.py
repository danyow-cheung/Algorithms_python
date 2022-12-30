import collections


class Solution(object):

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        hash_ = {}
        import re
        paragraph = re.sub(r'[^\w]', ' ', paragraph)
        paragraph = paragraph.lower().split()

        for i in paragraph:
            if i not in hash_:
                hash_[i] = 1
            else:
                hash_[i] += 1
        # print(hash_)
        target = ""
        for i in banned:
            target += i
        # print(target)
        for key, value in sorted(hash_.items(), key=lambda i: i[1], reverse=True):
            # print(key,type(key),type(target))
            if key in banned:
                continue
            else:
                return key


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

obj = Solution().mostCommonWord(paragraph,banned)