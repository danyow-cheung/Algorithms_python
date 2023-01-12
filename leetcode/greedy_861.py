class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = [0]*n


        # 橫
        for i in grid:
            if i[0]:
                for j in range(n):

                    ans[j]+=i[j]
            else:
                for j in range(n):
                    ans[j] += 1-i[j]
        ret = 0
        for i in range(n):
            ret += max(ans[-1-i],m-ans[-1-i])*(1<<i)
        print(ret)
        return  ret

        # 豎

grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
obj = Solution().matrixScore(grid)