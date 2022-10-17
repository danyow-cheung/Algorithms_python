class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        int_num1 = ""
        int_num2 = ""
        
        for i in num1:
            int_num1 += str(i)

        for i in num2:
            int_num2 += str(i)
        
        sum = int(int_num1)+int(int_num2)
        sum = str(sum)
        print(sum,type(sum))

num1 = '11'
num2 = '123'
obj = Solution().addStrings(num1,num2)