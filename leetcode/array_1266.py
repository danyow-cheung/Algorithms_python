class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        访问所有点的最小时间
        """
        for i in range(len(points)-1):

            print(points[i][0],points[i+1][0])
            print(points[i][1],points[i+1][1])
            # xDist = abs(points[i][0]-points[i+1][0])
            # print(xDist)
    def minTimeToVisitAllPoints_leetcode(self,points):
        res = 0
        n = len(points)
        for i in range(n - 1):
            xDist = abs(points[i][0] - points[i + 1][0])
            yDist = abs(points[i][1] - points[i + 1][1])
            res += max(xDist, yDist)

        return res

points = [[1,1],[3,4],[-1,0]]
obj = Solution().minTimeToVisitAllPoints(points)