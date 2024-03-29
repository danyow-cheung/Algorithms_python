class Solution(object):
    def second_big(self,nums,number):
        '''在剩下的nums里面找小于等于number'''
        res =0
        for i in nums:
            if i<=number:
                res = max(res,i)
        return res 

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        """
        ans = 0 
        for i in range(len(height)):
            area = 0
            j = self.second_big(height[i+1:],height[i])
            print("i={},j={},height[i]={},height[j]={}".format(i,j,height[i],height[j]))
            # print(height[i:j+1],height[i+1:])
            # length = len(height[i:j+1])


        
            # ans = max(ans,area)
        
        # print('final ans',ans)
    def maxArea_leetcode(self, height):
        res = 0 
        l = 0 
        r = len(height)-1 
        while l<r:
            area = (r-l)*min(height[l],height[r])
            res = max(res,area)
            if height[l]<height[r]:
                l+=1 
            else:
                r-=1 
        return res 
        

height = [1,8,6,2,5,4,8,3,7]
obj = Solution().maxArea(height)