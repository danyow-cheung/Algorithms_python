class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        ans = 0
        for i, j in zip(startTime, endTime):
            print(i, j)
            if queryTime in range(i, j + 1):
                ans += 1
        return ans

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
obj = Solution().busyStudent(startTime,endTime,queryTime)