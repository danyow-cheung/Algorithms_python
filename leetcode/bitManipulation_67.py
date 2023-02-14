class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        輸入是二進制
        
        """
        # 先把二進制轉換為10近制
        a = int(a,2)
        b = int(b,2)
        # 獲得相加數字之後再轉換為二進制

        # print(bin(10+11))
        return bin(a+b)[2:]

a = "11" 
b = "1"

a = "1010" 
b = "1011"

obj = Solution().addBinary(a,b)