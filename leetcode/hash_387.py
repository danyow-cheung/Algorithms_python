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


    '''beblow are wrong '''
    def firstUniqChar_v3(self,s):

        hash_ = {}
        for i in s:
            if i not in hash_:
                hash_[i]=1
            else:
                hash_[i]+=1
            if hash_[i]>=2:
                del hash_[i]
        print(hash_)

        for i in s:
            if i in hash_:
                print(i)
                return i
        return -1

    def firstUniqChar_leetcode(self,s):
        count = collections.Counter(s)
        for idx,ch in enumerate(s):
            if count[ch]==1:
                return idx
        return -1



s = 'leetcode'
s = "loveleetcode"
s ="aadadaad"
obj = Solution().firstUniqChar_v3(s)