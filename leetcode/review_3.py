class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        找到最長不重複的子串,不重複的字串！
        """
        res = set([])
        '''用集合作為候選列，找到最長的，用暴力循環去解答'''
        for  i in range(len(s)):
            for j in range(i+1,len(s)):
                # print(s[i:j+1],s[j] in s[i:j])
                if s[j] not in s[i:j] and s[i:j+1] not in res:
                    # continue
                    res.add(s[i:j+1])
                # else:
                    # res.add(s[i:j+1])
        print('res',res)
        '''返回集合中最長長度'''
        print(max(len(i) for i in res))
        return max(len(i) for i in res)

s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
obj = Solution().lengthOfLongestSubstring(s)
        