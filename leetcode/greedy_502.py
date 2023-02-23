class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        map = {}
        for i , j in zip(profits,capital):
            print(i,j)
            map[j]=i #最小资本 :利润
        # print(map)

        #  k代表的是项目
        while k>0:
            if len(capital)!= 0 and w>=max(capital):
                w += map[max(capital)] 
                k-=1 
                capital.remove(max(capital))

            elif len(capital)!=0 and w >= min(capital):
                w += map[min(capital)] 
                k-=1 
                capital.remove(min(capital))
            else:
                break 
        # print(w)
        return w
    def findMaximizedCapital_leetcode(self, k, w, profits, capital):
        '''
        https://leetcode.com/problems/ipo/solutions/2959870/ipo/
        '''
        import heapq 

        n  = len(profits)
        projects = list(zip(capital,profits))
        projects.sort()
        q = []
        ptr = 0 
        for i in range(k):
            while ptr<n and projects[ptr][0]<=w:
                heappush(q,-projects[ptr][1])
                ptr+=1 
            if not q:
                break 
            w += -heappop(q)
        return w 



            



k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]

k = 1
w = 2
profits = [1,2,3]
capital = [1,1,2]


obj = Solution().findMaximizedCapital(k,w,profits,capital)