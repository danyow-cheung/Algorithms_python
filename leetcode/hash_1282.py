class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        hash = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in hash:
                hash[groupSizes[i]] = [i] 
            else:
                hash[groupSizes[i]].append(i)
        
        print(hash)

        # for idx in hash.keys():
            # cur = hash[idx]
        #     res.append(hash[idx])
        # for i in res:
        #     if len(i)>=3:
        #         res.append(i[::3])
        #         del i 
        # print(res)
        import collections 
        hash = collections.defaultdict(list)

        for idx,val in hash.items():
            for i in range(len(val),idx):
                res.append(val[i:i+idx])
        print(res)
        return res 
groupSizes = [3,3,3,3,3,1,3]
# groupSizes = [2,1,3,3,3,2]
obj = Solution().groupThePeople(groupSizes)