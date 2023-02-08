class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        可以實現了但是超時
        """
        res= set()

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                print(s[i:j+1])
                
                if s[i:j+1]==s[i:j+1][::-1]:
                    print(s[i:j+1])
                    # return s[i:j+1]
                    res.add(s[i:j+1])
        
        if res:
            print(max(res, key=len))
            return(max(res, key=len))

        return s[0]


    def longestPalindrome_simple_brute_force(self, s):
        '''改進後的暴力循環
        不改了記答案'''
        if len(s)==1:
            return s 
            
        # cccc
        if len(set(s))==1:
            return s

            

        res = set() 
        for i in range(len(s)):
            left = 0
            
            # while left<=len(s):
            while left<len(s):
            
                left +=1 
                print(s[i:left+1])
                if s[i:left+1]==s[i:left+1][::-1]:
                    print('回文字符串=',s[i:left+1])
                    res.add(s[i:left+1])
                    break
        print(res)
        print(max(res, key=len))
        return max(res, key=len)

    def longestPalindrome_leetcode(self, s):
        res  = ""
        resLen = 0

        for i in range(len(s)):
            l,r = i ,i 
            
            # 基数列
            while l >= 0 and r < len(s) and s[l] == s[r]: # l在於等於0，r小於s的長度 以及左右相等
                if (r-l+1)>resLen: # 並且長度大於初始值
                    res = s[l:r+1] # 複製到res
                    resLen = r-l+1 # 更新resLen的長度
                l -= 1 # 更新索引
                r += 1
            
            # 偶数列
            l,r = i,i+1
            # 下面的操作和上述相同
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l+1)>resLen:

                    res = s[l:r+1]
                    resLen = r- l +1
                l -= 1
                r += 1
                
        return res


s = "babad"
s = "abcba"
s = "ccc"
s = 'bananas'

# obj = Solution().longestPalindrome(s)
obj = Solution().longestPalindrome_simple_brute_force(s)
