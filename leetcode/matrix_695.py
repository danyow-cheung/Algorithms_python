class Solution(object):
    def maxAreaOfIsland_dfs_recursive(self, grid):
        """
        如果我们在一个陆地正方形上，探索与之4方向相连的每个正方形
        （以及递归地与这些正方形相连的正方形，等等），
        那么探索的正方形总数将是该相连形状的面积。
        为了确保我们不会多次计算形状中的正方形，
        让我们使用seed来跟踪我们以前从未访问过的正方形。这也将防止我们多次计算同一形状。
        """
        seen = set()
        def area(r,c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                    return 0 
            seen.add((r,c))
            return (1+area(r+1,c)+area(r-1,c)+area(r,c-1) + area(r,c+1))
        return max(area(r,c) 
                    for r in range(len(grid))
                    for c in range(len(grid[0])))
    def maxAreaOfIsland_dfs_iterative(self, grid):
        '''我真的無語，都不知道套多少層了'''
        seen =set()
        ans = 0 
        for r0,row in enumerate(grid):
            for c0 ,val in enumerate(row):
                if val and (r0,c0) not in seen:
                    shape = 0
                    stack = [(r0,c0)]
                    seen.add((r0,c0))
                    while stack:
                        r,c = stack.pop()
                        shape +=1 
                        for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                            if (0<=nr<len(grid) and 0<= nc<len(grid[0])) and grid[nr][nc] and (nr,nc) not in seen:
                                stack.append((nr,nc))
                                seen.add((nr,nc))
                    ans = max(ans,shape)
        return ans 
    
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
obj = Solution().maxAreaOfIsland(grid)
