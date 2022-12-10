class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        返回元素的最大二进制的十进制模式
        """
        ans = "0"
        for i in n:
            if i > ans:
                ans = i
        return int(ans)
n = '32'
obj = Solution().minPartitions(n)