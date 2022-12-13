class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """

        def set_up_dict(items1):
            item_s1 = {}
            for i in range(len(items1)):
                item_s1[items1[i][0]] = items1[i][1]
            return  item_s1

        item_s1 = set_up_dict(items1)
        item_s2 = set_up_dict(items2)
        print(item_s1)
        print(item_s2)
        ret = []
        

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
obj= Solution().mergeSimilarItems(items1,items2)