class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        print(len(grid))

        if len(grid)==1:
            return 1
        # 橫
        for i in grid:
            print(i,type(i),i.count(0))
            # for j in i:
            #     print(j)
        # 豎

grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
obj = Solution().matrixScore(grid)