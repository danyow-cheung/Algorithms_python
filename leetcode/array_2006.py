class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        """
        res = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]-nums[j]==k or nums[i]-nums[j]==-k:
                    res +=1
        print(res)

nums = [1,2,2,1]
k = 1
obj = Solution().countKDifference(nums,k)