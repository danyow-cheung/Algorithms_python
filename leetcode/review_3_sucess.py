import collections
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        暴力循环容易懂但是超时
        https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/127839/longest-substring-without-repeating-characters/
        """

        def check(start,end):
            chars = set()
            for i in range(start,end+1):
                c = s[i]
                if c not in chars:
                    chars.add(c)
                else:
                    return False 
            return True 


        # 官方指导-暴力循环
        res =0 
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                if check(i,j):
                    # 和当前res做对比然后 取最大的
                    res = max(res,j-i+1)
        print(res)
        return res

    def lengthOfLongestSubstring_v2(self, s):
        '''
        滑动窗口-官方指导
        '''
        char = collections.Counter()
        left = right = 0 
        res =0 
        while right<len(s):
            r = s[right]
            char[r]+=1 
            while char[r]>1:     #这种情况就是不止一个
                l = s[left]
                char[l]-=1 
                left+=1 
            res = max(res,right-left+1)
            right+=1 
        return res 

    # 感觉看不懂居多 
    # 还是用回原来的方法吧

    def lengthOfLongestSubstring_v3(self, s):
        seen = set() # 集合保证元素不重复
        left  = 0 
        res = 0 
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[i])
                l+=1 # 前进一位
            seen.add(s[i])
            res =max(res,i-l+1)
        return res 
        
    
    
        

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# obj = Solution().lengthOfLongestSubstring(s)
obj = Solution().lengthOfLongestSubstring(s)