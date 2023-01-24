class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        # 構建初始矩陣
        matrix = [[-1] for i in range(cols)for j in range(rows)]
        print(matrix)
        # for i in matrix:
        #     print("i",i)
        # 根據r，cCenter定義為0
        matrix[rCenter][cCenter] = [0,0]
        
        
        print(matrix)
    def allCellsDistOrder_leetcode(self, rows, cols, rCenter, cCenter):
        '''https://leetcode.com/problems/matrix-cells-in-distance-order/solutions/278786/python-1-line-sorting-based-solution/'''
        def dist(point):
            pi,pj = point
            return abs(pi-rCenter)+abs(pj-cCenter)
        points =[(i,j) for i in range(rows) for j in range(cols)]
        return sorted(points,key=dist)
    
    
    def allCellsDistOrder_leetcode_bfs(self, rows, cols, rCenter, cCenter):
        '''
        https://leetcode.com/problems/matrix-cells-in-distance-order/solutions/278746/python-straightforward-dfs-bfs/
        '''
        def dfs(i,j):
            seen.add((i,j))
            res.append([i,j])
            for x,y in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0<=x <rows and 0<= y <cols and (x,y) not in seen:
                    dfs(x,y)
        res,seen = [],set()
        dfs(rCenter,cCenter)
        return sorted(res,key=lambda x:abs(x[0]-rCenter)+abs(x[1]-cCenter))

rows = 1
cols = 2
rCenter = 0
cCenter = 0
# 
# rows = 2
# cols = 2
# rCenter = 0
# cCenter = 1

obj = Solution().allCellsDistOrder(rows,cols,rCenter,cCenter)