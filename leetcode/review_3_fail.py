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

    def lengthOfLongestSubstring_v2(self, s):
        '''根据模板写滑动窗口https://blog.csdn.net/Scofield971031/article/details/107049033
        testcase-1出错'''
        
        def isValid(res):
            # 无效的情况就是列表里有重复的元素
            check = set()
            for i in res:
                if i not in check:
                    check.add(i)
                else:
                    return True
            return False

        left = 0 
        right = 0 
        res = []
        while right<len(s):
            res.append(s[right])
            right+=1 
            
            while isValid(res):     # 当前res无效的时候，弹出后一位,往前走一位
                res.pop(0)
                left+=1 

        print(res)
        print(len(res))
        

    
        

s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
# obj = Solution().lengthOfLongestSubstring(s)
obj = Solution().lengthOfLongestSubstring_v2(s)