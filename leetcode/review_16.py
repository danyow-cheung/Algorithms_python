class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import math 
        nums.sort()
        closest = float('inf')
        res = 0
        for ptr1 in range(len(nums)-2):
            cur_target = target - nums[ptr1]
            ptr2,ptr3 = ptr1+1,len(nums)-1
            while ptr3-ptr2>0:
                s = nums[ptr2]+nums[ptr3]
                if abs(cur_target-s)<closest:
                    closest = abs(cur_target-s)
                    res = s+nums[ptr1]
                if cur_target<s:
                    ptr3-=1 
                elif cur_target>s:
                    ptr2+=1 
                else:
                    return target
        return res 
    
        
nums = [-1,2,1,-4]
target = 1
obj = Solution().threeSumClosest(nums,target)
