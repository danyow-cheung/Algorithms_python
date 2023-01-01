import collections


class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        hash_ = {}
        for i in target:
            hash_[i] = 0

        print(hash_)
        for i in s:
            if i in hash_:
                hash_[i]+=1
        print(hash_)
        # count_val = collections.Counter(hash_.values())
        # print(count_val)
        if len(hash_)==1:
            if min(hash_.values())==len(target):
                return  1

        print(min(hash_.values()))


    def rearrangeCharacters_leetcode(self,s,target):
        maxx= []
        for i in range(len(set(target))):
            t_count = target.count(target[i])
            s_count = s.count(target[i])
            if t_count<= s_count:
                maxx.append(s_count//t_count)
            else:
                return  0
        print(maxx)
        return  min(maxx)

s = "ilovecodingonleetcode"
target = "code"
# s = "abcba"
# target = "abc"
s = "abbaccaddaeea"
target = "aaaaa"

s = "codecodecodecode"
target = "codecode"
obj = Solution().rearrangeCharacters_leetcode(s,target)