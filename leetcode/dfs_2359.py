class Solution(object):
    def dfs(self,node,edges,distance,visited):
        visited[node] = True 
        neighbor = edges[node]
        if neighbor!= -1 and visited[neighbor]==False:
            distance[neighbor]= distance[node]+1 
            self.dfs(neighbor,edges,distance,visited)
    
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        該問題呈現了一個帶有n節點的有向未加權圖。每個節點最多可以有一個出邊。我們的任務是從兩個給定節點中找到最近的節點，node1以便在所有節點上最小化與該節點的node2距離之間的最大值。如果有多個答案，我們需要返回索引最小的節點，如果不存在可能的答案，我們需要返回。node1,node2-1
        https://leetcode.com/problems/find-closest-node-to-given-two-nodes/solutions/3095888/day-25-graph-dfs-easiest-beginner-friendly-sol-o-n-time-and-o-n-space/
        """
        n = len(edges)
        ans = -1 
        minDist = float('inf')
        dist1 = [0]*n 
        dist2 = [0]*n 
        visited1 = [False]*n 
        visited2 = [False]*n 

        self.dfs(node1,edges,dist1,visited1)
        self.dfs(node2,edges,dist2,visited2)
        for curNode in range(n):
            if visited1[curNode] and visited2[curNode] and minDist>max(dist1[curNode],dist2[curNode]):
                minDist = max(dist1[curNode],dist2[curNode])
                ans = curNode
        return ans 

        
        

edges = [2,2,3,-1]
node1 = 0 
node2 = 1
obj = Solution().closestMeetingNode(edges,node1,node2)
