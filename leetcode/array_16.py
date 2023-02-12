class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        最接近的三數之和
        """
        z = float('inf')
        res = []
        '''這一步可以優化'''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                # print(nums[i],nums[j],nums[j+1:])
                pass 

        print(res)
        # var = float('inf')

    def threeSumClosest_leetcode(self, nums, target):
        nums.sort()
        closest = float('inf')
        res = 0
    
        for ptr1 in range(len(nums)-2):
            cur_target = target - nums[ptr1]
            ptr2, ptr3 = ptr1+1, len(nums)-1
            while ptr3 - ptr2 > 0:
                s = nums[ptr2] + nums[ptr3]
                if abs(cur_target - s) < closest:
                    closest = abs(cur_target - s)
                    res = s + nums[ptr1]
                if cur_target < s:
                    ptr3 -= 1
                elif cur_target > s:
                    ptr2 += 1
                else:
                    # found the closest sum possible; target itself
                    return target
                
        return res

    

nums = [-1,2,1,-4]
# nums = [0,0,0]
target = 1
obj = Solution().threeSumClosest(nums,target)