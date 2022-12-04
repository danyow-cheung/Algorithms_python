class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        left=0
        cur  = 0
        right = len(colors)-1
        # 从前往后遍历
        while left<right:
            if colors[left]!= colors[right]:
                # 获得第一组不同就直接返回
                cur = max(cur,(right-left))
            left+=1

        left = 0
        right = len(colors) - 1
        # 从后往前遍历
        while left<right:
            if colors[left]!= colors[right]:
                cur = max(cur,(right-left))
            right-=1
        print(cur)

        return cur


    def maxDistance_bruteForce(self,colors):
        ans = 0
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!= colors[j]:
                    cur = abs(i-j)
                    ans = max(ans,cur)
        print(ans)

# colors = [1,8,3,8,3]
colors = [1,1,1,6,1,1,1]
colors =[6,6,6,6,6,6,6,6,6,19,19,6,6]
obj = Solution().maxDistance(colors)