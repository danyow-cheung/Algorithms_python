class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        https://leetcode.com/problems/projection-area-of-3d-shapes/solutions/156732/projection-area-of-3d-shapes/

        """
        N = len(grid)
        ans = 0 
        for i in range(N):
            best_row = 0
            best_col = 0
            for j in range(N):
                if grid[i][j]:
                    ans +=1 
                best_row = max(best_row,grid[i][j])
                best_col = max(best_col,grid[j][i])
            ans += best_row+best_col
        return ans 
        
grid = [[1,2],[3,4]]
obj = Solution().projectionArea(grid)