class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for i in matrix:

            for j in range(1,n+1):
                print(i,j)
                if j not in i:
                    return False
        return True

    def checkValid(self,matrix):
        n = len(matrix)
        for row,col in zip(matrix,zip(*matrix)):
            if len(set(row))!= n or len(set(col))!=n:
                return False
        return True

matrix = [[1,2,3],[3,1,2],[2,3,1]]
obj = Solution().checkValid(matrix)