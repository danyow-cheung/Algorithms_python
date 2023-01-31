class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def convert(s):
            num =0 
            for i in s:
                num = num* 10+ord(i)-ord('0')
            return num 

        return convert(num1)* convert(num2)


num1 = "2"
num2 = "3"
obj = Solution().multiply(num1,num2)