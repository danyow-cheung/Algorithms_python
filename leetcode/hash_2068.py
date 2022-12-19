import collections


class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        count  ={}
        for i in word1:
            if i not in count:
                count[i] =1
            else:
                count[i]+=1
        print('对word1做字典之后的',count)
        # count1 = count.copy()
        for i in word2:
            if i not in count:
                count[i]=-1

            else:
                count[i]-=1

        print('与word2对比之后的',count)

        for key,value in count.items():
            if value>3 or value<-3:
                return False
        return True



word1 = 'aaaa'
word2 = 'bccb'
# word1 = "cccddabba"
# word2 = "babababab"
obj = Solution().checkAlmostEquivalent(word1,word2)