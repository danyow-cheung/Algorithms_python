import collections


class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        仅执行一次实现交换

        """
        if  collections.Counter(s1)!=collections.Counter(s2):
            return False
        hash_ ={}
        for i in range(len(s1)):
            hash_[s1[i]] = i

        print(hash_)
        ans = []
        for i in range(len(s2)):
            if s2[i] in hash_ and i != hash_[s2[i]]:
                ans.append([s2[i],i])
        print(ans,len(ans))

        if len(ans)==2 or len(ans)==0:
            return True
        return False





s1 = "bank"
s2 = "bank"

s2 = "kanb"
# s1 ="abcd"
# s2 = "dcba"
s1 = "siyolsdcjthwsiplccjbuceoxmpjgrauocx"
s2 ="siyolsdcjthwsiplccjbuceoxmpjgrauocx"
objc = Solution().areAlmostEqual(s1,s2)