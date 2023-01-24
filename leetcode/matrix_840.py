class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if m==1:
            return 0 

        for i in range(m):
            for j in range(n):
                print(grid[i],grid[i][j])
    
    def numMagicSquaresInside_leetcode(self,grid):
        '''
        https://leetcode.com/problems/magic-squares-in-grid/solutions/208894/python-solution/
        '''
        cnt = 0 
        # 構建3x3方塊
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                temp_grid = [grid[i:i+k][j:j+3] for k in range(3)]
                if self.isMagicSquare(temp_grid):
                    cnt +=1 
        return cnt 
    def isMagicSquare(self,grid):
        flat = [num for row in grid for num in row]
        if sorted(flat)!=[1,2,3,4,5,6,7,8,9]:
            return False
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(row[i]for row in grid)for i in range(3)]
        diag_sums = [sum(grid[i][i] for i in range(3)),(grid[0][2] + grid[1][1] + grid[2][0])]
        row_sums.extend(col_sums)
        row_sums.extend(diag_sums)
        return len(set(row_sums))==1
        
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# grid = [[8]]

obj = Solution().numMagicSquaresInside_leetcode(grid)