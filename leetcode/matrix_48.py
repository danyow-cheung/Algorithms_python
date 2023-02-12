class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # print(matrix)
        m = len(matrix)
        n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         print(matrix[i][j],matrix[j][i])

        #         # matrix[j][n-i] = matrix[i][j] 
        # print(matrix)
        for i in range(n//2+n%2):
            for j in range(n//2):
                temp = matrix[n-j-1][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp 
                


matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution().rotate(matrix)