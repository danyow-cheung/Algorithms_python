class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = arr[:]
        arr.sort()
        print(arr)
        res = []
        for i in rank:
            # print(i,arr.index(i)+1)
            i = arr.index(i)
            res.append(i)
        print(rank,res)
        return  res


    def arrayRankTransform_leetcode(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {}
        cnt = 1
        for i in sorted(list(set(arr))):
            rank[i] = cnt
            cnt+=1
        print(rank)
        return [rank[i] for i in arr]

arr =[40,10,20,30]
arr = [37,12,28,9,100,56,80,5,12]
obj = Solution().arrayRankTransform_leetcode(arr)