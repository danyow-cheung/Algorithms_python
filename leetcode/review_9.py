class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        print(str_x,type(str_x))
        return str_x==str_x[::-1]
        
x = 121
obj = Solution().isPalindrome(x)