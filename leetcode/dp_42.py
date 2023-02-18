class Solution(object):
    def trap_2(self,height):
        '''
        https://leetcode.com/problems/trapping-rain-water/solutions/3052416/python-simple-solution-beats-100-two-pointers-explained/
        '''
        total_water = 0 
        left_wall = 0 
        right_wall = len(height)-1 
        max_left_wall = 0 
        max_right_wall = 0 
        while left_wall<right_wall:
            if height[left_wall]<=height[right_wall]:
                if height[left_wall]>=max_left_wall:
                    max_left_wall = height[left_wall]
                else:
                    total_water += max_left_wall - height[left_wall]
                left_wall +=1 
            else:
                if height[right_wall]>=max_right_wall:
                    max_right_wall = height[right_wall]
                else:
                    total_water += max_right_wall - height[right_wall]
                right_wall -=1 
        return total_water
        
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
