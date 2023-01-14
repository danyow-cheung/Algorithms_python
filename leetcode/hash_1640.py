class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """

        map = {x[0]:x for x in pieces}
        print(map)
        res = []
        for num in arr:
            res += map.get(num,[])
            # print(map.get(num,[]))
        print(res)
        return  res ==arr




arr = [15,88]
pieces = [[88],[15]]
obj = Solution().canFormArray(arr,pieces)