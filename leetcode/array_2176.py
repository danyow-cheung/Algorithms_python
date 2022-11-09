class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        统计数组中相等且可以被整除的数对
        """
        res =0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    print(i,j)
                    res +=1
        print(res)

nums = [3,1,2,2,2,1,3]
k =2
nums = [5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3]
k =7
obj = Solution().countPairs(nums,k)