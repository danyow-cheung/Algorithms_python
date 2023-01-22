# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        还是利用折半查询的方法
        """
        low = 0
        high = n
        while low < high:
            mid = (low+high)//2
            # 如果是真的,已经错了往前面再找
            if isBadVersion(mid):
                # 更新high为mid
                high = mid 
            # 如果是假的，证明错误还在后面
            else:
                low = mid+1
        return high 
    