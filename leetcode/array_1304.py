import random


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        【和为零的N个不同整数】
        给你一个整数 n，请你返回任意 一个由 n 个 各不相同的整数组成的数组，
        并且这 n 个数相加和为 0
        解析：是数学公式咧->A[i] = i * 2 - n + 1
        """

        res = [0]*n
        for i in range(n):
            res[i] = i*2 -n+1
        print(res)


        return res

n = 1
obj =Solution().sumZero(n)