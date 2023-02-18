class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        while n:
            # &：按位运算符，参与运算的两个值，如果相应位都为1，则该位的结果为1，否则为0
            n = ~(n-1)
            ans += 1
        return ans

    def reverserBits_leetcode(self,n):
        res = 0
        for _ in range(32):
            res = (res<<1)+(n&1)
            n>>=1
        return res 
         
