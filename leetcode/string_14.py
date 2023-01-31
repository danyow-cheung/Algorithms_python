class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        for i in range(0,len(strs[0])):
        
            tmp = strs[0][i]; 
            
            for j in range(0,len(strs)):
                if (len(strs[j]) == i or strs[j][i] != tmp):
                    return strs[0][:i];

        return strs[0]; s
        

strs = ["flower","flow","flight"]
obj = Solution().longestCommonPrefix(strs)