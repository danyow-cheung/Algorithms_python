import collections

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        res = [0]*k 
        
        # count = collections.Counter(logs[i] for i in logs)
        # print(count)

logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
obj = Solution().findingUsersActiveMinutes(logs,k)
