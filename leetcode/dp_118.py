class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [[1]*i for i in range(1,numRows+1)]
        print(dp)
        for i in range(len(dp[2:])):
            print(dp[i])
            for j in dp[i]:
                print('dp[j]',j)

    def generate_leetcode(self,numRows):
        output = []
        for i in range(numRows):
            if i==0:
                prev = [1]
                output.append(prev)
            else:
                cur = [1]
                j =  1
                while j<i:
                    cur.append(prev[j-1] + prev[j])
                    j+=1
                cur.append(1)
                output.append(cur)
                prev = cur
        return  output


numRows = 5
obj = Solution().generate(numRows)