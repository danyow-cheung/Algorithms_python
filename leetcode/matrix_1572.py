class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat[0])
        res = 0
        for i in range(n):

            # 主对角线上的和
            res += mat[i][i]
            # 副对角线上的和
            res += mat[i][n-1-i]
        # 偶数行
        if n%2==0:
            return res
        # 奇数行
        print(res - mat[n//2][n//2])


mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
# mat =[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
obj = Solution().diagonalSum(mat)