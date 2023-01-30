class Solution(object):
    def leetcode(self,grid):
        from collections import deque
        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1
        
        # number of columns
        cols = len(grid[0])
        
        # keep track of fresh oranges
        fresh_cnt = 0
        
        # queue with rotten oranges (for BFS)
        rotten = deque()
        
        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1
        
        # keep track of minutes passed.
        minutes_passed = 0
        
        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1
            
            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                # visit all the adjacent cells
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    # update the fresh oranges count
                    fresh_cnt -= 1
                    
                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2
                    
                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        
        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        rows = len(grid)
        if rows==0:
            return -1 
        cols  = len(grid[0])
        # keep track of fresh oranges
        fresh_cnt = 0

        # queue with rotten oranges
        rotten = deque()
        # 访问方格中所有的橙子
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    # 存储当前橙子的坐标在rotten中
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    fresh_cnt+=1 
        
        # keep track of minutes passed 
        minutes_passed = 0 

        # 如果rotten中有元素且fresh_cnt不为0
        while rotten and fresh_cnt>0:
            # 更新minutes_passed 
            minutes_passed +=1 
            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x ,y = rotten.popleft()
                # visit all the adjacent cells
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    # 计算腐蚀的坐标
                    xx = x+dx 
                    yy = y+dy 
                    # 忽略边界操作
                    if xx<0 or xx==rows or yy<0 or yy==cols:
                        continue
                    # 忽略为空或已经是腐蚀的
                    if grid[xx][yy]==0 or grid[xx][yy]==2:
                        continue
                    
                    # 更新fresh_cnt 
                    fresh_cnt-=1 
                    # 更新当前为rotten  
                    grid[xx][yy]==2 
                    
                    # 添加当前坐标到queue 
                    rotten.append((xx,yy))

        
        # return the number of minutes 
        return minutes_passed if fresh_cnt==0 else -1 




grid = [[2,1,1],[1,1,0],[0,1,1]]
obj = Solution().orangesRotting(grid)