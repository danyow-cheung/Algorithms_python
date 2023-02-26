class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix 
        # print(self.matrix)
        # print(len(matrix),len(matrix[0]))    

        self.dp = [[0]*(len(matrix[0])+1 )for i in range(len(matrix)+1)]
        # 计算前缀
        for r in range(len(self.dp)-1):
            for c in range(len(self.dp[0])-1):
                self.dp[r+1][c+1] = matrix[r][c]+self.dp[r][c+1]+self.dp[r+1][c]-self.dp[r][c]
            

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        计算矩阵元素的总和，左上角为(row1,col1),右下角为(row2,col2)
        可以但超时
        """
        ans= 0 
        for col in range(row1,row2+1):
            for row in range(col1,col2+1):
                # print(self.matrix[col][row])
                ans+= self.matrix[col][row]
        # print(ans)
        return ans 
    def sumRegion_leetcode(self,row1,col1,row2,col2):
        '''
        https://leetcode.com/problems/range-sum-query-2d-immutable/solutions/2104244/python-easy-with-explanation/
        '''
        return self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]+self.dp[row1][col1]
    
    


        
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]

row1 = 2
col1 = 1
row2 = 4
col2 = 3 

row1 = 1
col1 = 1
row2 = 2
col2 = 2 

row1 = 1
col1 = 2
row2 = 2
col2 = 4 

# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(row1,col1,row2,col2)

