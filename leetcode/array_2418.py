class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        按照身高输出名字
        """
        # 构建哈希表
        # key-身高
        # value-名字
        dict = {}
        for i in range(len(names)):
            dict[heights[i]]=names[i]
        print(dict)

        # 单取身高做sorted
        ans = []
        key_lst = sorted(dict.keys())
        print(key_lst)
        # 从高到低，从字典中取得
        for i in key_lst[::-1]:
            ans.append(dict[i])

        print(ans)
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
obj = Solution().sortPeople(names,heights)