import collections


class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = [words[0]]

        for i in range(len(words)-1):

            count1 = collections.Counter(words[i])
            count2 = collections.Counter(words[i+1])

            # print(words[i],words[i+1],count1==count2)
            if count1!=count2:
                res.append(words[i+1])

        print(res)
        return  res

words = ["abba","baba","bbaa","cd","cd"]
# words = ["a","b","c","d","e"]
obj =Solution().removeAnagrams(words)