class Solution(object):
    def gcdOfStrings_leetcode(self, str1, str2):
        if str1+str2!=str2+str1:
            return ""
        import gcd 

        # get the gcd of the two lengths
        max_length = gcd(len(str1),len(str2))# not work in python,but ok in python3 
        return str1[:max_length]
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        字符串的最大公因子
        """
        left = 0 
        ans =""
        while left<len(str1) and left<len(str2):
            # 如果此刻的元素相同
            if str1[left]==str2[left]:
                ans+=str1[left]
                left+=1
            else:
                break
        
        if len(ans)==0:
            return ans 
        
        print(left,ans)
        str1_flag = False
        str2_flag = False
        
        for i in range(len(str1)):
            if i*ans == str1:
                str1_flag=True
                break
                
        for i in range(len(str2)):
            if i*ans == str2:
                str2_flag = True
                break

        if str1_flag and str2_flag:
            return ans 
        


str1 = "ABCABC"
str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"

# str1 = 'LEET'
# str2 = 'CODE'

obj = Solution().gcdOfStrings(str1,str2)