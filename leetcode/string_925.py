class Solution(object):
    def isLongPressedName(self, name, typed):

        """
        :type name: str
        :type typed: str
        :rtype: bool
        检测name是否有在typed中出现过，可以出现多次但不能不出现
        """
        # 差集
        # print(list(set(typed).difference(set(name))))
        # 并集
        # print(list(set(name).union(set(typed))))
        # 交集
        # print(list(set(name).intersection(set(typed))))

        i = j = 0
        while (i<len(name) and j<len(typed)):
            if typed[j] == name[i]:
                while j+1<len(typed) and typed[j]==typed[j+1]:
                    j+=1
                    # 有連續重複字母的特殊情況
                    if i+1<len(name) and name[i] ==name[i+1]:
                        i+=1
                else:
                    i+=1
                    j+=1
            else:
                return False
        return i==len(name) and j==len(typed)





name = "alex"
typed = 'aaleex'
obj = Solution().isLongPressedName(name,typed)