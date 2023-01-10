class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        learning:https://leetcode.com/problems/find-the-town-judge/solutions/242938/java-c-python-directed-graph/
        Consider trust as a graph, all pairs are directed edge.
        The point with in-degree - out-degree = N - 1 become the judge.

        """
        count = [0]*(n+1)
        print(count)
        for i,j in trust:
            print(i,j)
            count[i] -=1
            count[j]+=1
        print(count)
        for i in range(1,n+1):
            if count[i] ==n-1:
                print(i)
                return i
        return -1

n = 2
trust = [[1,2]]

n = 3
trust = [[1,3],[2,3]]

n = 3
trust = [[1,3],[2,3],[3,1]]

obj = Solution().findJudge(n,trust)