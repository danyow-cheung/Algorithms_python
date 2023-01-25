import collections

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        https://leetcode.com/problems/longest-repeating-character-replacement/solutions/2805777/longest-repeating-character-replacement/

        """
        start = 0 
        frequency_map = {}
        max_freq = 0 
        longest_substring_length = 0 
        for end in range(len(s)):
            # 初始化
            frequency_map[s[end]] = frequency_map.get(s[end],0)+1 

            max_freq = max(max_freq,frequency_map[s[end]])

            # 移動start指針往右邊如果當前窗口有效
            is_valid = (end+1-start-max_freq<=k)
            if not is_valid:
                frequency_map[s[start]]-=1 
                start +=1 
            # 當前窗口有效，存儲窗口長度
            longest_substring_length = end+1-start
        return longest_substring_length
        



s = "ABAB"
k = 2

s = "AABABBA"
k = 1

obj = Solution().characterReplacement(s,k)
