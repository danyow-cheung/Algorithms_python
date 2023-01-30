class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
        """
        # def bfs(r,c):
        #     if mat[r][c]==1:
        #         return True
        #     # 中间不是边缘
        #     if r>0 and c<len(mat[0]):
        #         bfs(r-1,c)
        #         bfs(r+1,c)
        #         bfs(r,c-1)
        #         bfs(r,c+1)
            
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if bfs(i,j):
        #             pass 
        # 跟着学吧，别自己瞎来
        '''官方教程-Brute force'''
        rows = len(mat)
        if rows==0:
            return mat 
        cols = len(mat[0])
        # 初始化
        # dist = [[0 for j in range(rows)]for i in range(cols)]
        dist =  mat[:]
        print(dist)

        for i in range(rows):
            for j in range(cols):
                # 本身是0的，距离0的距离也是0
                if mat[i][j]==0:
                    dist[i][j]=0 
                else:
                    for k in range(rows):
                        for l in range(cols):
                            if mat[k][l]==0:
                                dist_01 = abs(k-i)+abs(l-j)
                                dist[i][j] = min(dist[i][j],abs(k-i)+abs(l-j))

        print(dist)

        return dist 


    def updateMatrix_bfs(self, mat):
        '''https://leetcode.com/problems/01-matrix/solutions/1369741/c-java-python-bfs-dp-solutions-with-picture-clean-concise-o-1-space/'''
        import collections
        m = len(mat)
        n = len(mat[0])
        DIR = [0,1,0,-1,0]

        q = collections.deque([])
        for r  in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    q.append((r,c))
                else:
                    # 标记为未记录
                    mat[r][c]=-1
        while q:
            r,c = q.popleft()
            for i in range(4):
                nr,nc = r+DIR[i].c+DIR[i+1]
                if nr<0 or nr==m or nc<0 or nc==n or mat[nr][nc]!=-1:
                    continue
                mat[nr][nc]==mat[r][c]+1
                q.append((nr,nc))
        print(mat)

        return mat 
    def updateMatrix_dp(self, mat):
        import math
        m = len(mat)
        n = len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] >0:
                    top = mat[r-1][c] if r>0 else math.inf 
                    left = mat[r][c-1] if c>0 else math.inf 
                    mat[r][c] = min(top,left)+1 
        for i in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if mat[r][c]>0:
                    bottom = mat[r+1][c] if r<m-1 else math.inf 
                    right = mat[r][c+1] if c<n-1 else math.inf 
                    mat[r][c] = min(mat[r][c],bottom+1,right+1)
        print(mat)
        
        return mat 

mat = [[0,0,0],[0,1,0],[0,0,0]]

mat = [[0,0,0],[0,1,0],[1,1,1]]
obj =  Solution().updateMatrix_dp(mat)
