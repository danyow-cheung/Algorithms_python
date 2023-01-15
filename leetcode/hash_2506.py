import collections


class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(words)):

            count =  collections.Counter(words[i])
            for j in range(i+1,len(words)):
                # print(words[i],words[j])
                # if words[j]
                diff = collections.Counter(words[j])
                # print(len(count),len(diff))
                # print(count.keys()==diff.keys())
                if count.keys()==diff.keys():
                    res += 1
        return  res
words = ["aba", "aabb", "abcd", "bac", "aabc"]
obj = Solution().similarPairs(words)