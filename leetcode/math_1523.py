class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        

        '''TimeExceedLimit'''
        # for i in range(low,high+1):
        #     if i%2!=0:
        #         print(i)
        #         res+=1 
        # return res 

        diff = high - low 
        if low%2:
            diff+=1 
        if high%2:
            diff+=2 
        return diff//2 
        

            
low = 3
high = 7
obj = Solution().countOdds(low,high)