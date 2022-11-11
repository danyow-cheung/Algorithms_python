import collections


class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        可以形成最大正方形的矩形数目

        """
        res = []
        for i in range(len(rectangles)):
            # print(rectangles[i])
            res.append(min(rectangles[i]))
            # print(k)
            # for j in rectangles[i]:
            #     # if k<= j
            #     print(j)
        print(res)
        # dict_ = dict(res)
        count = collections.Counter(res)
        # print(max(count.values()))
        # print(max(count.keys()))
        max_val = max(count.keys())
        print(max_val,count[max_val])
rectangles = [[5,8],[3,9],[5,12],[16,5]]
rectangles = [[2,3],[3,7],[4,3],[3,7]]
rectangles = [[5,8],[3,9],[3,12]]
obj = Solution().countGoodRectangles(rectangles)