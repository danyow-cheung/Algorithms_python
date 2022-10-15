class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(f"原始序列{nums}")

        left = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[left],nums[i] = nums[i],nums[left]
                left+=1
                print(nums) 
        
    def moveZeros_v2(self,nums):
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(0)
        print(nums)
        
nums = [0,1,0,3,12] 
obj = Solution().moveZeroes(nums)