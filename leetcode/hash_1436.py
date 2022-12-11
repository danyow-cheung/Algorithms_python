class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        dest = dict()

        for start,end in paths:
            if start not in dest:
                dest[start] =2
            else:
                dest[start]+=1
            if end not in dest:
                dest[end] =1
            else:
                dest[end]+=1
        print(dest)
        for k,v in dest.items():
            if v == 1:
                return k


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
paths = [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]
obj = Solution().destCity(paths)