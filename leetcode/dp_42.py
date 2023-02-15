class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        真的寄
        https://leetcode.com/problems/trapping-rain-water/solutions/127551/trapping-rain-water/
        c++ -> python
        """
        ans = 0 
        size = len(height)

       
        
        for i in range(1,size-1):
            left_max= 0
            right_max = 0
            # 左邊遞減
            for j in reversed(range(0,i)):
                left_max = max(left_max,height[j])

            # 右邊遞增
            for j in range(i,size):
                right_max = max(right_max,height[j])
            
            ans += min(left_max,right_max) - height[i]
        print(ans)
        return ans 




height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj = Solution().trap(height)
