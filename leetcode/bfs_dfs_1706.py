class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        
        def check(row,col):
            if row==m:
                return col 
            
            # 注意：grid包含1和-1，代表右边和左边
            # 将grid[row][col]添加到当前的col得到new_cols
            new_col = col + grid[row][col]

            # 如果new_Col超标
            if new_col==n or new_col==-1 or grid[row][new_col]!=grid[row][col]:
                return -1 
            else:
                return check(row+1,new_col)
        res = []
        for i in range(n):
            res.append(check(0,i))
        return res 
        
            

grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
obj = Solution().findBall(grid)
