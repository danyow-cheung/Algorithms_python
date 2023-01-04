class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        完全不知道怎么写阿，老铁
        """
        # map = ['a','b','i','o','u']
        #ref:https://leetcode.com/problems/count-sorted-vowel-strings/solutions/2027288/python-4-approaches-dp-maths/
        dp = [[0]*6 for i in range(n+1)]
        print(dp)
        for i in range(1,6):
            dp[1][i] =i
        print(dp)
        for i in range(2,n+1):
            dp[i][1] = 1
            for j in range(2,6):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        print(dp)
        return dp[n][5]

    def countVowelStrings_v2(self,n):
        dp = [1]* 5
        for _ in range(1,n):
            for i in range(1,5):
                dp[i] = dp[i]+dp[i-1]
        print(dp)
        print(sum(dp))

n = 1
n = 2
obj = Solution().countVowelStrings_v2(n)