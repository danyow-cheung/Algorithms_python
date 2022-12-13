class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        import collections
        count = collections.Counter(arr)
        print(count)
        ans = set()
        for key,value in count.items():
            print(count[key],count[key+1])
            if count[key] not in ans:
                ans.add(count[key])
            elif count[key] in ans:
                return False 

        # print(ans)

        return True 


arr = [1,2,2,1,1,3]
arr = [-1,4,-5,11,-3,4,-1,5,0,11,3]
obj= Solution().uniqueOccurrences(arr)