class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            left = i+1 
            right = n-1 
            if nums[i]>0:
                break
            if i>=1 and nums[i]==nums[i-1]:
                continue
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total>0:
                    right -= 1
                elif total<0:
                    left+=1 
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans 
    


nums = [-1,0,1,2,-1,-4]
obj = Solution().threeSum(nums)
