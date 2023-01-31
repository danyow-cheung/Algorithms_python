class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        # 選擇的球員得分
        dp = []
        hash = dict()
        
        for i,j in zip(scores,ages):
            print(i,j)
    
    def bestTeamScore_leetcode(self, scores, ages):
        from bisect import bisect_right

        new_lst =sorted(zip(ages,scores))
        visited = [new_lst[0][1]]
        dp = [new_lst[0][1]]
        ans  = new_lst[0][1]
        for i in range(1,len(new_lst)):
            s = new_lst[i][1]
            index = bisect_right(visited,s)
            curr = max(dp[:index]) + s if index else s 
            ans = max(ans,curr)
            visited.insert(index,s)
            dp.insert(index,curr)
        return ans 

        



        
scores = [1,3,5,10,15]
ages = [1,2,3,4,5]

scores = [4,5,6,5]
ages = [2,1,2,1]
obj = Solution().bestTeamScore_leetcode(scores,ages)
