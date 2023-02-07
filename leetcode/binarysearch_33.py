class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # ans = nums.index(target)
        # return ans if ans else -1 
        # l = 0 
        # r = len(nums)-1
        # ans= 0
        # while l<=r:
        #     mid = (l+r)//2 
        #     if nums[mid]>target:
        #         l = mid + 1 
        #     elif nums[mid]<target:
        #         r = mid -1 
        #     else:
        #         ans = l 

        # print(l,r,ans)
        try: return nums.index(target)
        except ValueError: return -1

nums = [4,5,6,7,0,1,2]
target = 0
# target = 9

obj = Solution().search(nums,target)
