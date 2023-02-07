class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #集合保障不重複
        seen = set()
        l = 0 
        res = 0 
        for i in range(len(s)):
            # 出現相同元素的時候
            while s[i] in seen:
                #移除元素
                seen.remove(s[l])
                # 下標加1
                l = l+1 
            seen.add(s[i])
            res = max(res,i-l+1)
        return res         

        
s = "abcabcbb"
# s = 'bbbbbb'
# s = "pwwkew"

obj = Solution().lengthOfLongestSubstring(s)