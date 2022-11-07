class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        解码异或后的数组
        """
        arr = []
        for i in range(len(encoded)):
            if i+1 <len(encoded):
                arr.append(encoded[i]^encoded[i+1])
        print(arr)

encoded = [1,2,3]
first = 1
obj = Solution().decode(encoded,first)
