class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1 
        while left<=right:
            print('nums',nums)
            if nums[left]<nums[right]:
                left +=1 
            elif nums[left]>nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                left +=1 
                right -=1 
            
        print(nums)

    def sortColors(self,nums):
        '''https://leetcode.com/problems/sort-colors/solutions/26481/python-o-n-1-pass-in-place-solution-with-explanation/'''
        # 使用了三指針
        red = 0 
        white =   0 
        blue = len(nums)-1 
        while white <=blue:
            if nums[white]==0:
                nums[red],nums[white] = nums[white],nums[red]
                red +=1 
                white+=1 
            elif nums[white]==1:
                white+=1 
            else:
                nums[white],nums[blue] = nums[blue],nums[white]
                blue -=1 
                

nums = [2,0,2,1,1,0]
# nums = [2,0,1]

obj = Solution().sortColors(nums)