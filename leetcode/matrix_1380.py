class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_ans = []
        m = len(matrix)
        n = len(matrix[0])

        # minimum element in its row 
        for i in range(m):
            min_ans.append(min(matrix[i]))
        
        max_ans =[]
        for i in range(n):
            mx = []
            for j in range(m):    
                mx.append(matrix[j][i])
            # print(max(mx))
            max_ans.append(max(mx))
        
        print(min_ans,max_ans)
        # return 
        print(list(set(min_ans).intersection(set(max_ans))))
matrix = [[3,7,8],[9,11,13],[15,16,17]]
# matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]

obj = Solution().luckyNumbers(matrix)