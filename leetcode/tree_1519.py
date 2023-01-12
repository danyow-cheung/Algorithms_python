import string


class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        子樹中標籤相同的節點數
        https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solutions/2864718/number-of-nodes-in-the-sub-tree-with-the-same-label/

        """
        graph = [[] for _ in range(n)]

        for a,b in edges:
            print(graph)
            graph[a].append(b)
            graph[b].append(a)
        counts = [0]*len(string.ascii_lowercase)
        answer =[0]*n
        def dfs(node,parent):
            index = ord(labels[node]) - ord('a')
            previous = counts[index]
            counts[index]+=1

            for child in graph[node]:
                if child!=parent:
                    dfs(child,node)
            answer[node] = counts[index]-previous
        dfs(0,-1)
        return  answer

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
obj = Solution().countSubTrees(n,edges,labels)