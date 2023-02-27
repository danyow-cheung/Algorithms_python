class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

        如果小数部分为循环小数，则将循环的部分括在括号内。

        如果存在多个答案，只需返回 任意一个 。

        对于所有给定的输入，保证 答案字符串的长度小于 104 。
        https://leetcode.com/problems/fraction-to-recurring-decimal/solutions/51187/python-easy-to-understand-solution/
        
        """
        if numerator % denominator==0:
            return str(numerator//denominator)
        sign = ''if numerator * denominator >=0 else '-'
        numerator,denominator = abs(numerator),abs(denominator)
        res = sign+str(numerator//denominator)+'.'
        numerator %= denominator 
        i,part = 0,''
        m = {numerator:i}
        while numerator % denominator:
            numerator *=10
            i+=1 
            rem = numerator % denominator
            part += str(numerator//denominator)
            if rem in m:
                part = part[:m[rem]] + '('+part[m[rem]:]+')'
                return res + part 
            m[rem]=i 
            numerator = rem 
        return res + part 


numerator = 1
denominator = 2
obj = Solution().fractionToDecimal(numerator,denominator)