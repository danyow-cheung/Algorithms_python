class Solution(object):
    def isLongPressedName(self, name, typed):

        """
        :type name: str
        :type typed: str
        :rtype: bool
        检测name是否有在typed中出现过，可以出现多次但不能不出现
        """
        # 差集
        print(list(set(typed).difference(set(name))))
        # 并集
        print(list(set(name).union(set(typed))))
        # 交集
        print(list(set(name).intersection(set(typed))))


name = "alex"
typed = 'aaleex'
obj = Solution().isLongPressedName(name,typed)