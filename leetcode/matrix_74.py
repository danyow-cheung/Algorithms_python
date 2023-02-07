class Solution(object):
    def serchMatrix_twopointer(self,matrix,target):
        l = 0 
        r = len(matrix)-1 
        col = -1 
        while l<=r:
            mid = (l+r)//2 
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                col = mid 
            if matrix[mid][-1]<target:
                r = mid +1 
            else:
                l = mid -1 
        l = 0 
        r= len(matrix[0])-1 
        while l<=r:
            mid = (l+r)//2
            if matrix[col][mid]==target:
                return True
            if matrix[col][mid]<target:
                l = mid+1 
            else:
                r = mid-1 
        return False
        
         
    def serchMatrix_simple_(self,matrix,target):
        '''這個是怎麼通過的沒想到真沒想到'''
        temp=[]
        for i in matrix:
            for j in i:
                temp.append(j)
        if target in temp:return True
        else:return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        print(matrix[m//2][0])

        if (matrix[m//2][0])>target:
            # 目標數值大於target先後找
            print(matrix[m//2+1][0])
        elif matrix[m//2][0]==target:
            return True
        else:
            # 目標數值小於target先前找
            print(matrix[m//2-1][-1])



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
obj = Solution().searchMatrix(matrix,target)