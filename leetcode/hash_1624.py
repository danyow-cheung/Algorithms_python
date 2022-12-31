class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_ = {}
        for i in range(len(s)):
            print(s[i])
            if s[i] not in hash_:
                hash_[s[i]] = i
            else:

                hash_[s[i]]-=i
        print(hash_)
        max_val = min(hash_.values())

        print(max_val)
        if max_val<0:
            return abs(max_val+1)
        # for value in hash_.values():
        #     if value<0:
        #         return abs(value+1)
        return  -1


    def maxLengthBetweenEqualCharacter(self,s):
        dic = dict()
        maxer = -1
        for i, val in enumerate(s):
            if val in dic:
                diff = i - dic[val] - 1
                maxer = max(maxer, diff)
            else:
                dic[val] = i
        return maxer

s = 'aa'
# s = 'abca'
s = 'cabbac'

obj = Solution().maxLengthBetweenEqualCharacters(s)