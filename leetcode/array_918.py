class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         Kadane's algorithm is used to finding the maximum sum subarray from a given array.
        环形子数组的最大和
        """
        max_val = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                # print(nums[i],nums[j])
                print(nums[i:j])
                curr = sum(nums[i:j])
                max_val = max(max_val,curr)
        print(max_val)

    def maxSubarraySumCircular_approach1(self,nums):
        '''Approach 1: Enumerate prefix and suffix sums
        '''
        n = len(nums)
        right_max = [-1]* n
        right_max[n-1] = nums[n-1]
        print(right_max)
        for i in range(0,len(nums),2):
            suffix_sum = nums[n-1]
            suffix_sum += nums[i]
            right_max[i] = max(right_max[i+1],suffix_sum)
        print(right_max)
        max_sum = nums[0]
        special_sum = nums[0]
        # for i in range


    def maxSubarraySumCircular_approach2(self,nums):
        '''calculate the mininum subarray'''
        cur_max ,cur_min ,sum_val =0,0,0
        max_sum = nums[0]
        min_sum = nums[0]
        for num in nums:
            cur_max = max(cur_max,0)+num
            max_sum = max(max_sum,cur_max)
            cur_min = min(cur_min,0)+num
            min_sum = min(min_sum,cur_min)
            sum_val += num
        print(sum_val,)
        if sum_val==min_sum:
            print(max_sum)
        else:
            print(max(max_sum,sum_val-min_sum))

# nums = [1,-2,3,-2]
nums = [5,-3,5]
obj = Solution().maxSubarraySumCircular_approach2(nums)