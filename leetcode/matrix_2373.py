class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        给你一个大小为 n x n 的整数矩阵 grid 。

        生成一个大小为 (n - 2) x (n - 2) 的整数矩阵  maxLocal ，并满足：

        maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
        换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。

        返回生成的矩阵。

        """
        # print(len(grid))
        maxLocal = len(grid)-2
        ans = []

        for i in range(maxLocal):
            res = []
            for j in range(maxLocal):
                k = []
                k.append(grid[i][j])
                k.append(grid[i][j+1])
                k.append(grid[i][j+2])

                k.append(grid[i+1][j])
                k.append(grid[i+1][j+1])
                k.append(grid[i+1][j+2])

                k.append(grid[i + 2][j])
                k.append(grid[i + 2][j + 1])
                k.append(grid[i + 2][j + 2])
                m = max(k)
                res.append(m)
            ans.append(res)
        print(ans)

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
obj = Solution().largestLocal(grid)