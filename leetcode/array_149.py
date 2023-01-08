import collections
import math


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        遍歷所有點。設當前點為points[i]。維護一個哈希映射cnt來計算角度。
            對於每個j ≠ i 計算 atan2 of the vector[points[j] - points[i]]並將此值添加到哈希映射中。
            讓k是hash map中某個角度值的最大出現次數。
            更新答案k + 1個. (+ 1 +1+ 1因為點points[i]也在線上，我們必須將其包含在答案中。）

        """
        n = len(points)
        if n==1:
            return  1

        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j!= i:
                    # print(points[j][1],points[j][0],points[i][1],points[i][0])
                    # math.atan2: 以弧度返回 y/x 的反正切值：
                    cnt[math.atan2(points[j][1] - points[i][1],points[j][0] - points[i][0])] += 1
            result = max(result,max(cnt.values())+1)
            print("cnt=",cnt)
        print("result",result)
        return result

points = [[1,1],[2,2],[3,3]]

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
obj = Solution().maxPoints(points)