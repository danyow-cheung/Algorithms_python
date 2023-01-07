class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = []
        ans.append(nums[0]+nums[-1])

        for i in range(1,len(nums)//2):

            print(nums[i],nums[-i-1])
            ans.append(nums[i]+nums[-i-1])
        print(ans)
        print(max(ans))
        return max(ans)

nums = [3,5,2,3]
# nums = [3,5,4,2,4,6]
obj = Solution().minPairSum(nums)