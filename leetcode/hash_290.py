class Solution(object):
    def wordPattern_wrong(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        res_dict  = {}
        s = s.split()
        res = []
        for i in range(len(pattern)):
            if pattern[i] not in res_dict.keys() :
                #if s[i]!= res_dict.popitem()[1]:
                res_dict[pattern[i]] = s[i]
            
            else:
                res.append(s[i]==res_dict.get(pattern[i]))
        print(res_dict,res)
        # print(res_dict.get('a'),res_dict.get('b'),res_dict.popitem()[1])

        if False in res:
            return False
        else:
            return True
    def wordPattern_leetcode(self,pattern,s):
        s = s.split()
        res = {}
        if len(pattern)!=len(s):return False
        if len(set(pattern))!=len(set(s)):return False 

        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]]=pattern[i]
            elif res[s[i]]!=pattern[i]:
                return False
        print(res)
        return True 
pattern = 'abba'
s = "dog cat cat dog"

# pattern = "abba"
# s = "dog cat cat fish"
# s = "dog dog dog dog"
obj = Solution().wordPattern_leetcode(pattern,s)
