class Solution(object):
    def spiralOrder_leetcode(self, matrix):
        '''https://leetcode.com/problems/spiral-matrix/solutions/3039684/python-solution-explained-step-by-step-with-illustrations/
        '''
        res = []
        while matrix:
            # 1 
            res += matrix.pop(0)
            # 2 
            if matrix and matrix[0]:
                for line in matrix:
                    res.append(line.pop())
            # 3 
            if matrix:
                res += matrix.pop()[::-1]
            # 4 

            if matrix and matrix[0]:
                for line in matrix[::-1]:
                    res.append(line.pop(0))
        print(res)
        return res 


    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        # mat = [[0 for i in range(n)]for j in range(m)]
        mat =[]
        print(mat)

        for i in range(m):
            for j in range(n):
                print(matrix[i][j])
                mat.append(matrix[i][j])
                if j==n-1:
                    for ii in range(i):
                        mat.append(matrix[ii][j])
        print("mat=",mat)
                

matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution().spiralOrder_leetcode(matrix)