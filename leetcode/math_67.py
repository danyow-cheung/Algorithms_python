class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
           
        # Calculating binary value using function
        # 2表示2进制，int转化为整数
        print(int(a,2))
        print(int(b,2))

        sum = bin(int(a, 2) + int(b, 2))
        
        # Printing result
        print(sum)
        print(sum[2:])  
        return sum[2:]   

a = '11'
b= '1'
obj = Solution().addBinary(a,b)