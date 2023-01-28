import collections

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # https://leetcode.com/problems/finding-the-users-active-minutes/solutions/2599209/python-solution/
        cnt = {}
        for i in logs:
            if i[0] in cnt:
                if i[1] not in cnt[i[0]]:
                    cnt[i[0]].append(i[1])
                elif i[1] in cnt[i[0]]:
                    continue
            else:
                cnt[i[0]] = [i[1]]
        print(cnt)
        uam_cnt =[len(i) for i in cnt.values()]
        set_uam = collections.Counter(uam_cnt)
        ans  = [0]*k      
        for i in range(1,k+1):
            if set_uam[i]:
                ans[i-1] = set_uam[i]
        return ans 
        
        
        

logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
obj = Solution().findingUsersActiveMinutes(logs,k)
