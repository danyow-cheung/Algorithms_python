import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]]=1
            elif hash[s[i]]>=1:
                hash[s[i]]+=1
        # for key,value in
        print(hash)

        ans = -1
        for i in hash.keys():
            if i==1:
                ans = s.find(i)
                break
        print(ans)
    def firstUniqChar_v2(self,s):
        count = collections.Counter(s)
        ans = []
        print(count)
        for i in count.keys():
            if count[i]==1:
                ans.append(i)
        print(ans)
        if len(ans):

            final = s.find(ans[0])
        else:
            final = -1
        print(final)

s = 'leetcode'
s = "loveleetcode"
s = 'aabb'
obj = Solution().firstUniqChar_v2(s)