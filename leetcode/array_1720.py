class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        解码异或后的数组
        还是不太懂什么叫做位运算？
        """
        res = [first]
        # print(res)
        for a in encoded:
            print(res[-1],a)
            res.append(res[-1]^a)
        print(res)
        return res

encoded = [1,2,3]
first = 1
obj = Solution().decode(encoded,first)
