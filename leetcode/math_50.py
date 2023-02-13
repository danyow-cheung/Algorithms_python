class Solution(object):
    def myPow_v1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        不通過
        https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/
        """

        # while n>0:
        #     print('x',x)
        #     x *= float(x) 
        #     n-=1 
        # print(x,type(x))
        # return x 

        
        pow = 1 
        for i in range(n):
            pow = pow*x 
        return pow 
    def myPow_v2(self, x, n):
        '''不通過'''
        if n==0:
            return 1 
        if x==0:
            return 0 
        return x* self.myPow_v2(x,n-1)

    def myPow(self,x,n):
        '''final'''
        return x**n

x = 2.00000
n = 10
x = 2.10000
n = 3
obj = Solution().myPow(x,n)