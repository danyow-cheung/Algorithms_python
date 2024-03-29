class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/3231791/240-time-91-4-and-space-98-52-solution-with-step-by-step-explanation/
        """
        row = 0
        col = len(matrix[0])-1 
        while row<len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True 
            elif matrix[row][col]<target:
                row+= 1 
            else:
                col -=1 
        return False 


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
obj = Solution().searchMatrix(matrix,target)