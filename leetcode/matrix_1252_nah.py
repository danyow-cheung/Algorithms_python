class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        奇数值单元格的数目
        给你一个 m x n 的矩阵，最开始的时候，每个单元格中的值都是 0。

        另有一个二维索引数组 indices，indices[i] = [ri, ci] 指向矩阵中的某个位置，
        其中 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。

        对 indices[i] 所指向的每个位置，应同时执行下述增量操作：

        ri 行上的所有单元格，加 1 。
        ci 列上的所有单元格，加 1 。
        给你 m、n 和 indices 。请你在执行完所有 indices 指定的增量操作后，
        返回矩阵中 奇数值单元格 的数目。
        """
        # 构建模型
        mtx = []
        m_mtx = []*m
        n_mtx = [0]*n
        for i in range(m):
            mtx_1 = []
            for j in range(n):
                mtx_1.append(0)
            mtx.append(mtx_1)
        print("原始矩阵",mtx)


        for i in range(n):
            # print(mtx[i])
            for j in range(m):
                # print(mtx[i][j])
                # print(i,j)
                add_j= 0
                add_i = 0
                if [i,j] in indices:
                    print([i,j])
                    mtx[i][j]+=1
                    add_i = i
                    add_j = j
                mtx[i][add_j]+=1
            # mtx[add_i]+=1
        print(mtx)
        # print(indices[0],indices[0][0])
    def oddCells_leetcode(self,m,n,indices):
        x,y = [0]*n,[0]*m
        for r,c in indices:
            x[r]+=1
            y[r]+=1
        print(x,y)
        print(sum([(r+c)%2 for c in y for r in x]))

m = 2
n = 3
indices = [[0,1],[1,1]]
obj = Solution().oddCells_leetcode(m,n,indices)