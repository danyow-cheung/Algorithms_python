class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = self.convet_dict(s)
        t_dict = self.convet_dict(t)

        t_val = self.calcu_number(t_dict)
        s_val = self.calcu_number(s_dict)
        
        print(s_dict,"\n",t_dict)
        
        # 字母出现元素，次数相同的情况下，再考虑数值是否相同
        if len(s_dict.keys())== len(t_dict.keys()) and t_val == s_val:
            idx = self.dict(s,t)
            # 探究是否是按顺序的
            for i in range(len(t)):
                if t[i]!=idx[t[i]]:
                    print(t[i])
                    return False
 
        else:
            
            return True  

    def dict(self,s,t):
        i = 0 
        idx = {}
        while i <len(s):
            # e作为索引，t作为数值
            if s[i] in idx:
                continue
            else:
                idx[s[i]]=t[i]
            i+=1 
        print(idx)
    
    def calcu_number(self,s):
        res = 0
        for i in s.values():
            res += i 

        return res 
            
    def convet_dict(self,s):
        s_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1 
            else:
                s_dict[s[i]] += 1 

        return s_dict

    def isIsomorphic_v2(self, s, t):
        i = 0 
        idx = {}
        while i <len(s):
            # e作为索引，t作为数值
            if s[i] in idx:
                continue
            else:
                idx[s[i]]=t[i]
            i+=1 
        print(idx)
        
        for i in range(len(t)):
            if t[i]!=idx[s[i]]:
                print(t[i]+idx[s[i]])
                return False 

        return True
            
    def isIsomorphic_leetcode(self, s, t):
        s_dict = {}
        t_dict = {}

        for c1,c2 in zip(s,t):
            if (c1 not in s_dict )and (c2 not in t_dict):
                s_dict[c1] = c2 
                s_dict[c2] = c1 

            elif s_dict.get(c1)!= c2 or t_dict.get(c2)!=c1:
                return False 
        return True


    def isIsomorphic_leetcode22(self, s, t):

        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):

            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False

        return True
        


s = "egg"
t = "add"

s = "bbbaaaba"
t = "aaabbbba"

obj = Solution().isIsomorphic_leetcode(s,t)
