

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        

        res  = ''
        for i in digits:
            res  =  res + str(i) 
        
        print(res,type(res))
        res = int(res)+1
        print(res,type(res))
        res = [int(x) for x in str(res)]
        print(res)

digits =[1,2,3]
digits= [9,9]
obj = Solution().plusOne(digits)