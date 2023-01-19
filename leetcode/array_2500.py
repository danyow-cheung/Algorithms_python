class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # ans = 0
        for i in range(m):
            # print(grid[i])
            grid[i].sort()

        s = 0
        while n>0:
            l = []
            for i in range(m):
                l.append(grid[i][n-1])

            s+=max(l)
            l = []
            n-=1
        print(s)
        return s


# grid = [[1, 2, 4], [3, 3, 1]]
grid = [[10]]
# grid = [[9,81],[33,17]]
obj = Solution().deleteGreatestValue(grid)