class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。
        如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。
        """
        max_num = min(a,b)
        res = []
        for i in range(1,max_num+1):
            if a % i == 0 and b%i ==0:
                res.append(i)
        
        return len(res)
a = 12 
b = 6 
a = 25 
b = 30
obj = Solution().commonFactors(a,b)
