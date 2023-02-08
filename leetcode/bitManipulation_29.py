class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        兩數相除，但是不能使用內置函數
        還是不太懂even though
        https://leetcode.com/problems/divide-two-integers/solutions/2719043/python-subtraction-o-logn/
        """
        a = abs(dividend)
        b = abs(divisor)
        print(a,b)

        negative = (dividend<0 and divisor>=0) or (dividend>=0 and divisor<0)
        output = 0 
        while a>=b:
            counter = 1 
            decrement =b 
            # 當a大於decrement
            while a>= decrement:
                a -= decrement  # a遞減
                output += counter
                
                counter += counter
                decrement += decrement
        output = output if not negative else -output
        return min(max(-2147484648,output),2147483647)




dividend = 10
divisor = 3
obj = Solution().divide(dividend,divisor)
