class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        units_val = 0
        # 按照numberOfUnitsPerBoxi進行排序，大的先
        # boxTypes.sort(key=lambda x: x[1], reverse=True)
        # boxTypes.sort(key=lambda x: x[1])
        ss = sorted(boxTypes,key=lambda x:x[1])
        # [[1, 3], [2, 2], [3, 1]]

        print(boxTypes)
        i = 1
        while truckSize>0 and i<= len(boxTypes):
            # 貪心局部最優找最大的索引為1的值
            if truckSize - ss[-i][0] >= 0:
                truckSize -= ss[-i][0]
                units_val += ss[-i][0] * ss[-i][1]
                i+=1
            else:
                units_val += truckSize*ss[-i][1]
                truckSize = 0
        print(units_val)
        return units_val


# boxTypes = [[1,3],[2,2],[3,1]]

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
boxTypes = [[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]]

'''
[[5, 10], [2, 5], [4, 7], [3, 9]]
[[2, 5], [4, 7], [3, 9], [5, 10]]
'''
size = 13
obj = Solution().maximumUnits(boxTypes,size)