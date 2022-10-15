from ast import Str
from unittest import result


class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        
        string = ""
        while columnNumber>0:
            columnNumber -=1 
            # 65是a的阿斯科码
            
            string = chr(65+columnNumber%26)+string
            columnNumber = columnNumber//26
        return string 
        
num = 1 
num= 701
obj = Solution().convertToTitle(num)