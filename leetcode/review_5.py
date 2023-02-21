class Solution(object):
    def longestPalindrome_new(self, s):
        '''https://leetcode.com/problems/longest-palindromic-substring/solutions/900639/python-solution-with-detailed-explanation-using-dp/'''
        # 常学常新
        dp = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=True
        print(dp)
        
        ans = s[0]
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=True
                    if j-i+1>len(ans):
                        ans = s[i:j+1]
        print(ans)

        return ans 



    def longestPalindrome(self, s):
        """
        题目提醒动态规->work但是超时
        """
        left = 0
        # 初始化dp数组，原始数值是每个元素本身
        # dp = [[i] for  i in s ]
        dp = []
        print(dp)
        
        for i in range(len(s)):
            # print(dp[i])
            left = i +1
            cur = ""
            while left<=len(s):
                print(s[i:left])
                cur = s[i:left] if s[i:left]==s[i:left][::-1] else cur 

                left+=1
            print('cur',cur)
            # dp[i] = cur 
            dp.append(cur)

        # 里面存储的是 每个元素的最长回文子字符串
        print(dp)
        

        # max_len  = max(len(i) for i in dp)
        # print(max_len)
        # for i in dp:
        #     if len(i)==max_len:
        #         print('final',i)
        #         return i 
        '''以下这一大串可以更改为'''
        print(max(dp,key=len))


        # for i in range(len(s)):
    def longestPalindrome_brute_force(self, s):
        '''最长回文子串 ok但是超时'''
        if len(s)==1:
            return s 

        res = []
        '''暴力循环来一遍'''
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    # curr = s[i:j+1] 
                    res.append(s[i:j+1])
        if len(res)==0:
            return s[0]
        # 找到最长的子元素然后返回
        # return res[0]
        max_len  = max(len(i) for i in res)
        print(max_len)
        # print(i for i in res if len(i)==max_len)  
        for i in res:
            if len(i)==max_len:
                print(i)
                return i 

    def test(self,s):
        """
        题目提醒动态规->work但是超时
        """
        left = 0
        dp=""
        
        for i in range(len(s)):
            left = i +1
            cur = ""
            while left<=len(s):
                # print(s[i:left])
                cur = s[i:left] if s[i:left]==s[i:left][::-1] else cur 
                left+=1 
            dp = max(dp,cur,key=len)
        # 里面存储的是 每个元素的最长回文子字符串
        print(dp)
        return dp 


        


s = "babad"
# s = 'cbbd'
# s='ac'
# s='a'

# obj = Solution().longestPalindrome(s)
obj = Solution().test(s)
