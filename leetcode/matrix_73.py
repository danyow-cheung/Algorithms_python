class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        def dfs(x,y):
            # 元素是0，上下左右都要變成零
            if matrix[x][y]==0:
                '''這塊說我最大回溯深度超過？'''
                if n>x>0 and n>y>0:
                    dfs(x-1,y,)
                    dfs(x+1,y,)
                    dfs(x,y-1,)
                    dfs(x,y+1,)
            # 將元素設為0

            matrix[x][y]=0 
        for i in range(m):
            for j in range(n):
                dfs(i,j)

    def setZeros(self,matrix):
        '''https://leetcode.com/problems/set-matrix-zeroes/solutions/177436/set-matrix-zeroes/'''
        R = len(matrix)
        C = len(matrix[0])
        rows,cols = set(),set()


        for i in range(R):
            for j in range(C):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        
        
            

matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution().setZeroes(matrix)
