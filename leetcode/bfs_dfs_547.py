class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        https://leetcode.com/problems/number-of-provinces/solutions/303150/python-union-find-dfs-bfs/

        """

        m = len(isConnected)
        seen = set()
        def dfs(p):
            for q,adj in enumerate(isConnected[p]):# enumerate->index，val
                # print('i,adj',i,adj)
                if adj==1 and (q not in seen):
                    seen.add(q)
                    dfs(q)
        cnt = 0 
        for i in range(m):
            if i not in seen:
                dfs(i)
                cnt+=1 
        print(cnt)

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
obj = Solution().findCircleNum(isConnected)
