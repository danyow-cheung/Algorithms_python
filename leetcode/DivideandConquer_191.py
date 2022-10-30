class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        位运算
        """
        ans = 0
        while n:
            # &：按位运算符，参与运算的两个值，如果相应位都为1，则该位的结果为1，否则为0
            n &= (n-1)
            ans += 1
        return ans

