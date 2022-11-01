from itertools import count
from re import S


class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # 获取每个元素
        flatten_lst = [j for sub in mat for j in sub]
        print(flatten_lst)
        # 如果给的参数不可能实现，直接返回原矩阵
        if r*c!=len(flatten_lst):
            return mat 
        else:
            res =[]
            count = 0
            # 用个巧，循环构造list
            for i in range(r):
                i_lst =[]
                for j in range(c):
                    i_lst.append(flatten_lst[count])
                    count+=1
                res.append(i_lst)
            print(res)

mat = [[1,2],[3,4]]
r = 2
c = 4
obj = Solution().matrixReshape(mat,r,c)