class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            print(grid[i].count(1))
    def islandPerimeter_leetcode(self, grid):
        # https://leetcode.com/problems/island-perimeter/solutions/3046548/python-solution-beats-100/

        perimeter = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    perimeter+=4 
                    # 上
                    if i>0 and grid[i-1][j]==1:
                        perimeter -=2 
                    # 左
                    if j>0 and grid[i][j-1]==1:
                        perimeter-=2
        return perimeter
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
obj = Solution().islandPerimeter(grid)