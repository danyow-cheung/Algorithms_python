import collections


class Solution(object):
    def add(self,ans,key,value):
        while value>0:
            ans.append(key)
            value-=1
        return ans

    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(arr1)
        ans =[]
        print(count)
        for i in range(len(arr2)):
            if count[arr2[i]]:
                ans.append([arr2[i]]*count[arr2[i]])

        print(ans)
        res = []
        for i in ans:
            for j in i:
                res.append(j)

        print(res)

        for key,value in sorted(count.items(),key=lambda x:x[0]):
            if key not in res:
                self.add(res,key,value)


        print(res)


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
arr2 = [2,42,38,0,43,21]
obj = Solution().relativeSortArray(arr1,arr2)