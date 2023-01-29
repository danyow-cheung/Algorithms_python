class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # subtring = self.getSubstring(s1)
        # hash_26 = {}
        import collections
        s1_c = collections.Counter(s1)
        s2_c = collections.Counter(s2)
        
        keys = [i for i in s1_c.keys()]
        vals = [i for i in s1_c.values()]
        
        print(keys)
        # if s2_c[i for i in keys]:
            # print(s1_c[i])
        for i in keys:
            if s2_c[i]:
                print(s2_c[i],s1_c[i])
            else:
                return False

        print(s1_c,s2_c)

    def getSubstring(self,s1):
        print(s1)
        res = []
        # 添加倒序
        res.append(s1[::-1])
        # 添加原字符串
        res.append(s1)
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                print(s1[i:j+1])
        print('res',res)
        return res 


    def checkInclusion_leetcode(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        if n1>n2:return False

        s1Count = [0]*26 
        s2Count = [0]*26 
        # 初始化滑動窗口的第一個值
        for i in range(n1):
            s1Count[ord(s1[i])-ord('a')]+=1
            s2Count[ord(s2[i])-ord('a')]+=1
        print(s1Count)
        print(s2Count)
        #n2-n1是滑動窗口的步長
        
        for i in range(n2-n1):
            if s1Count==s2Count:
                return True
            # 減少次數
            s2Count[ord(s2[i])-ord('a')]-=1 
            s2Count[ord(s2[i+n1])-ord('a')]+=1 
        return s1Count==s2Count



s1 = "ab"
s2 = "eidbaooo"
# obj = Solution().checkInclusion(s1,s2)
obj = Solution().checkInclusion_leetcode(s1,s2)
