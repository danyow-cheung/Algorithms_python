import collections


class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        hash_ ={}
        ans = 0

        for i in words1:
            if i not in hash_:
                hash_[i]=1
            elif hash_[i]:
                hash_[i]+=1
        print(hash_)

        for key,value in hash_.items():
            if value>=2:
                # 出现多次的元素赋值为负数
                hash_[key]=-1

        print(hash_)
        for i in words2:
            if hash_[i]>0:
                hash_[i]+=1
        print(hash_)
        for key,value in hash_.items():
            if value==2:
                ans+=1
        print(ans)
        return ans

    def countWords_v2(self,words1,words2):
        ans = 0
        count_s1 = collections.Counter(words1)
        count_s2 = collections.Counter(words2)
        print(count_s1)
        print(count_s2)

        for key1,value1 in count_s1.items():
            for key2,value2 in count_s2.items():
                if key1==key2 and value2==value1==1:
                    ans +=1
        print(ans)
        return ans

words1 =['leetcode','is','amazing','is','as']
words2 = ['amazing','leetcode','is']
obj = Solution().countWords_v2(words1,words2)