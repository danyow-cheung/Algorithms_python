class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]
        print(row_maxes,col_maxes)
        # for col in zip(*grid):
        #     print(col)

        return sum(min(row_maxes[r],col_maxes[c]) - val
                   for r,row in enumerate(grid)
                   for c,val in enumerate(row)
                   )

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
obj = Solution().maxIncreaseKeepingSkyline(grid)