import collections


class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1_count = collections.Counter(s1.split())
        # s2_count = collections.Counter(s2.split())
        print(s1_count)
        for i in s2.split():
            if s1_count[i]:
                s1_count[i]+=1
            elif s1_count[i] ==0:
                s1_count[i]=1
        print(s1_count)
        ans = []
        for key,value in s1_count.items():
            if value==1:
                ans.append(key)

        return ans

s1 = "this apple is sweet"
s2 = "this apple is sour"
obj = Solution().uncommonFromSentences(s1,s2)