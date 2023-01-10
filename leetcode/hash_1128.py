class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        time exceed limit
        """
        ans =0
        for i in range(len(dominoes)):
            for j in range(i+1,len(dominoes)):
                print(dominoes[i],dominoes[j])
                if (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]):
                    ans +=1
        print(ans)

    def numEquivDominoPairs_leetcode(self, dominoes):
        d = {}
        cnt = 0
        for a,b in dominoes:
            key = min(a,b) *10 + max(a,b)
            if key in d:
                cnt += d[key]
                d[key]+=1
            else:
                d[key]=1
        print(d)
        return cnt


dominoes = [[1,2],[2,1],[3,4],[5,6]]
dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]

obj = Solution().numEquivDominoPairs_leetcode(dominoes)