import collections


class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        返回是按照vlaue的升序
        """
        dict_ = collections.defaultdict(int)
        res = []

        for weight, value in items1:
            dict_[weight] += value

        for weight, value in items2:
            dict_[weight] += value
        print(dict_)

        for weight in sorted(dict_.keys()):
            res.append([weight, dict_[weight]])
        return res

        

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
obj= Solution().mergeSimilarItems(items1,items2)