class Solution(object):
    def isBoomerang_wrong(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def loop_(lst):
            let_set = set(lst)
            if len(let_set)==1:
                return 1 
            return -1
        res =[]
        for i in points:
            res.append(loop_(i))
        print(res)
        
        # if -1 in res:
        #     return True
            
        # else:
        #     return False
        return True if -1 in res else False

    def isBoomerang(self,points):
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        # 斜率判断是否为直线
        return (y2-y1)*(x3-x2)!=(y3-y2)*(x2-x1)
points = [[1,1],[2,3],[3,2]]
points = [[1,1],[2,2],[3,3]]

# points = [[0,0],[2,1],[2,1]]
obj = Solution().isBoomerang(points)