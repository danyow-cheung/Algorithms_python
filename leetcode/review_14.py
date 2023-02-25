class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        没有脑子不会写了
        """
        for i in range(0,len(strs[0])):
            # 第一个元素
            temp = strs[0][i]
            
            for j in range(0,len(strs)):
                # 第二个元素到后面的
                # print(strs[j])
                if (len(strs[j])==i or strs[j][i]!=temp):
                    return strs[0][:i]
        return strs[0]
    






strs = ["flower","flow","flight"]
obj=Solution().longestCommonPrefix(strs)