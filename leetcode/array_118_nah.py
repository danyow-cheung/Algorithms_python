class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res = []
        flag = 0 
        if numRows==1:return res.append([1])
        while flag < numRows:
            if flag == 0:
                res.append([1])
                            
            flag+=1 

        print(res)

        
obj = Solution().generate(numRows = 5)