import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        
        需要統計p的數量和個數
        TLE
        """ 
        ans = []
        left = 0 
        # set up the dict-p 
        # dict_p = {}
        # for i in p:
        #     if i not in dict_p:
        #         dict_p[i]=1 
        #     else:
        #         dict_p[i]+=1 
        dict_p = collections.Counter(p)

        n = len(p)
        def check_dict(lst):
            
            count = collections.Counter(lst)
            if (count==dict_p):
                return True
            return False

        while left<len(s):
            if check_dict(s[left:left+n]) :
                ans.append(left)
            left+=1 
        return ans 

    def findAnagrams_leetcode(self, s, p):
        '''tle'''
        ls = len(s)
        lp = len(p)
        if ls<lp:
            return
        ans = []
        cp = collections.Counter(p)
        for i in range(ls-lp+1):
            cs = collections.Counter(s[i:i+lp])
            if cs == cp:
                ans.append(i)
        return ans 
    def findAnagrams_leetcode2(self, s, p):
        s_dict = collections.Counter(s[:len(p)-1])
        p_dict = collections.Counter(p)
        start = 0 
        res = []
        for i in range(len(p)-1,len(s)):
            s_dict[s[i]] += 1
            # checking if counters match
            if s_dict == p_dict:
                res.append(start)
            # remove the first element from counter
            s_dict[s[start]] -= 1
            #if element count = 0, pop it from the counter
            if s_dict[s[start]] == 0:
                del s_dict[s[start]]
            start += 1
            
        return res





s = "cbaebabacd"
p = "abc"

# s = "abab"
# p = "ab"

# s = 'baa'
# p = 'aa'

# s = "ababababab"
# p = 'aab'

obj = Solution().findAnagrams(s,p)
