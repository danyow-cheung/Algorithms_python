import collections


class Solution(object):
    def minTime_DepthFirstSearch(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        这太难了直接看解析吧
        https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solutions/3033301/python3-dfs-explained/

        """
        # 使用边缘edges来构建树
        # 因为树是undirected，我们需要在树上添加方向
        tree  = collections.defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        # 节点node是当前节点我们需要处理的
        # par是节点node的直接母节点
        def dfs(node,par):
            res = 0
            # 因为构建的树，所有没有环
            # 然而因为树是undirected，這意味著鄰居節點之一是其父節點。
            for nei in tree[node]:
                # 我们不回溯到母节点
                if nei!= par:
                    res +=  dfs(nei,node)
            # 情况1：res!=0,意味着我们在树上找到了苹果
            # 情况2：hasApple[node]==True，意味当前节点上有苹果
            # 在上述的情况下，增加res+2
            # 添加2的原因是，我们需要一个1来到节点，一个回溯
            if res or hasApple[node]:
                return  res +2
            # 在当前节点上没有苹果，并且后续也没有返回0
            return  res
        # 按照 dfs，你可以看到當我們回到節點 0 時，如果樹上有一些蘋果，
        # 我們在結果中加了一個額外的 2，所以這裡需要 -2。
        # 如果這棵樹上沒有蘋果，dfs 會返回 0，但我們不能返回 -2，所以只返回 0
        return  max(dfs(0,-1)-2,0)



n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
obj = Solution().minTime_DepthFirstSearch(n,edges,hasApple)