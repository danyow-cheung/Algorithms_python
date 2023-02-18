import collections
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        移除最多的同行或同列石头
        https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solutions/2814101/python-easy-solution/

        """
        x,y=collections.defaultdict(list),collections.defaultdict(list)
        for i in stones:
            x[i[0]].append(i[1])
            y[i[1]].append(i[0])
        neighbour,visited=0,set()
        for i in stones:
            if (i[0],i[1]) not in visited:
                q=collections.deque()
                q.append(i)
                while q:
                    stonex,stoney=q.popleft()
                    if (stonex,stoney) not in visited:
                        visited.add((stonex,stoney))
                        for j in x[stonex]:
                            q.append([stonex,j])
                        for j in y[stoney]:
                            q.append([j,stoney])
                neighbour+=1
        return len(stones)-neighbour

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
obj = Solution().removeStones(stones)