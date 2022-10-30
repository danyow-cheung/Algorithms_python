class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        for i in range(30):
            if 2**i==n:
                print(i)
                return True 
        return False 
n = 1 
# n = 16
# n =3 
obj = Solution().isPowerOfTwo(n)
