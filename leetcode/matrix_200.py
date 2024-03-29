class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: 
    给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
    岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
    此外，你可以假设该网格的四条边均被水包围。
    """
    if not grid:
      return 0 
    
    count = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j]=='1':
          self.dfs(grid,i,j)
          count +=1 
    return count 
  
  def dfs(self,grid,i,j):
    if i<0 or j<0 or i>=len(grid)or j>=len(grid[0]) or grid[i][j]!='1':
      return
    grid[i][j]='#'
    self.dfs(grid,i+1,j)
    self.dfs(grid,i-1,j)
    self.dfs(grid,i,j+1)
    self.dfs(grid,i,j-1)
    
    



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

obj = Solution().numIslands(grid)