from collections import defaultdict


class Graph:
    def __init__(self,val) -> None:
        self.graph = defaultdict(list)
        self.val = val 

    def addEdge(self,u,v):
        self.graph[u].append(v)

    #topologicalSort使用的递归函数
    def topologicalSortUtil(self,v,visited,stack):
        # 标记当前节点是访问过的
        visited[v] = True
        # 回溯所有方塊？
        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)

        stack.append(v)
    
    # 拓扑排序的函数。它使用递归
    # topologicalSortUtil ()
    def topologicalSort(self):
        # 將設所有方塊都是沒訪問過的
        visited = [False]*self.val 
        stack = []

        #调用递归helper函数来存储topology
        #从所有顶点开始逐个排序
        for i  in range(self.val):
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)
        # 打印
        print(stack[::-1])



class Solution_dfs(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        拓撲排序 (Topological sorting)
        https://leetcode.com/problems/course-schedule-ii/solutions/205947/course-schedule-ii/
        """

        

class Solution_node_indegree(object):
    WHITE = 1 
    GRAY  = 2 
    BLACK = 3

    def findOrder_dfs(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        拓撲排序 (Topological sorting)
        https://leetcode.com/problems/course-schedule-ii/solutions/205947/course-schedule-ii/
        """
        # 创建图的邻接表表示
        adj_list = defaultdict(list)

        # 输入中的对[A, b]表示从b开始的边——> A
        for dest,src in prerequisites:
            adj_list[src].append(dest)
        
        topological_sorted_order = []
        is_possible =True 

        # 默認情況下都是White
        color = {k:Solution_dfs.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible
            # 如果我们已经找到一个循环，就不要进一步递归
            if not is_possible:
                return
            # 開始遞歸
            color[node] = Solution_dfs.GRAY 

            # #遍历相邻顶点
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor]==Solution_dfs.WHITE:
                        dfs(neighbor)
                    elif color[neighbor]==Solution_dfs.GRAY:
                        is_possible= False
            
            # 遞歸結束，把這個標記為黑色
            color[node] = Solution_dfs.BLACK 
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # 如果節點是沒使用的，調用遞歸函數
            if color[vertex]==Solution_dfs.WHITE:
                dfs(vertex)
        return topological_sorted_order[::-1]if is_possible else []  


numCourses = 2
prerequisites = [[1,0]]
obj = Solution_dfs().findOrder(numCourses,prerequisites)