from collections import defaultdict


class Graph:
    def __init__(self,val) -> None:
        self.graph = defaultdict(list)
        self.val = val 

    def addEdge(self,u,v):
        self.graph[u].append(v)

    #基于回溯的拓扑排序
    def topologicalSortUtil(self,v,visited,stack):
        # 标记当前节点是访问过的
        visited[v] = True
        
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        拓撲排序 (Topological sorting)

        """
        if len(prerequisites)==0:
            return [0]
        



        def dfs(cur,prev):
            pass 




numCourses = 2
prerequisites = [[1,0]]
obj = Solution().findOrder(numCourses,prerequisites)