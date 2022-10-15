class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # num = [2,3,5]
        # if n==1:return True 
        # # 现整除，查看余数如果在就是True
        # res = n//2 

        # if res in num:
        #     return True
        # else:
        #     res = n//2 
        #     self.isUgly(res)
        # return False 
        if n<=0:return False 
        for i in [2,3,5]:
            # 循環繼續除
            while n%i ==0:
                n = n//i
             
        return n == 1

n = 6 
n = 8
obj = Solution().isUgly(n)