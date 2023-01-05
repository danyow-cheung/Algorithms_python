class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """

        matrix = [[0]*len(colSum) for i in range(len(rowSum))]
        print(matrix)
        for i in range(len(matrix)):
            print(matrix[i])
            if sum(matrix[i]) == rowSum[i]:
                print("ok")

        for i in range(len(matrix)):
            print(matrix[i])
        # for i in range(1,10):
        #     for element in matrix:
        #         print(element)

    def restoreMatrix_v2(self, rowSum, colSum):
        n = len(rowSum)
        m = len(colSum)

        ans = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                val = min(rowSum[i],colSum[i])
                rowSum[i] -= val
                colSum[j] -= val
                ans[i][j] = val
                print("ans = ",ans)

        print(ans)

    def restoreMatrix_v3(self, rowSum, colSum):
        '''
        for each result value at A[i][j]
        we greedily take the min(row[i], col[j]).
        Then we update the row sum and col sum:
        row[i] -= A[i][j]
        col[j] -= A[i][j]
        '''
        n = len(rowSum)
        m = len(colSum)

        ans = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= ans[i][j]
                colSum[j] -= ans[i][j]
        return ans



rowSum = [3,8]
colSum = [4,7]


# rowSum = [5,7,10]
# colSum = [8,6,8]
obj = Solution().restoreMatrix_v2(rowSum,colSum)