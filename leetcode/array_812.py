class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        x_max = max(i[0]for i in points)
        y_max = max(i[1]for i in points)
        x_min = min(i[0]for i in points)
        y_min = min(i[1]for i in points)
        diff_x = x_max-x_min
        diff_y = y_max-y_min
        print(diff_x*diff_y*1/2)
        return diff_x*diff_y*1/2

    def leetcode(self,points):
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1] - j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
                       for i, j, k in itertools.combinations(p, 3))

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
points = [[1,0],[0,0],[0,1]]
obj = Solution().largestTriangleArea(points)