class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        ---這不是直接寄你爹----
        太平洋大西洋水流問題
        --------------------
        有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。

        这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。

        岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

        返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可流向大西洋 。
        """
        m = len(heights)
        n = len(heights[0])

        def dfs(i,j,prev,coords):
            if i<0 or i==m or j<0 or j==n:
                # 超标
                return
            if (i,j) in coords:
                # 已经走过该坐标
                return 
            # 得到此刻的高度
            height = heights[i][j]

            if height<prev:
                # 水流不能流向更高的地方
                return 

            # 当前位置是可以添加到coords的
            coords.add((i,j))
            # 四个方向的迭代
            dfs(i+1,j,height,coords)
            dfs(i-1,j,height,coords)
            dfs(i,j+1,height,coords)
            dfs(i,j-1,height,coords)
            
        pacific = set()
        # 上row
        for i in range(n):
            dfs(i,0,0,pacific)
        atlantic = set()
        
        # right col 
        for i in range(m):
            dfs(i,n-1,0,atlantic)
        # bottom row 
        for j in range(n):
            dfs(m-1,j,0,atlantic)
        # 交并区域?
        return list(pacific&atlantic)



class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        
        def dfs(i, j, prev_height, coords):
            if i < 0 or i == m or j < 0 or j == n:
                # out of bounds
                return
            
            if (i, j) in coords:
                # already visited
                return
            
            height = heights[i][j]
            
            if height < prev_height:
                # water can't flow to a higher height
                return
            
            # ocean is reachable from current coordinate
            coords.add((i, j))
            
            # all four directions
            dfs(i + 1, j, height, coords)
            dfs(i - 1, j, height, coords)
            dfs(i, j + 1, height, coords)
            dfs(i, j - 1, height, coords)
            
        pacific_coords = set()
        
        # top row
        for j in range(n):
            dfs(0, j, 0, pacific_coords)
        
        # left col
        for i in range(m):
            dfs(i, 0, 0, pacific_coords)
            
        atlantic_coords = set()
            
        # right col
        for i in range(m):
            dfs(i, n - 1, 0, atlantic_coords)
            
        # bottom row
        for j in range(n):
            dfs(m - 1, j, 0, atlantic_coords)
            
        # intersection of coords reachable from both Pacific and Atlantic
        return list(pacific_coords & atlantic_coords)
        
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
obj = Solution().pacificAtlantic(heights)
