from collections import defaultdict
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        https://leetcode.com/problems/bus-routes/solutions/127510/bus-routes/?envType=study-plan&id=level-2
        """
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0
        routes = map(set, routes)
        graph = defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in xrange(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1


routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
obj = Solution().numBusesToDestination(routes,source,target)