class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        此版本可以通過testcase
        """
        if len(nums)==1:
            # 只存在一個數字並且不為1？直接返回1 
            if nums[0]>1:return 1 

        max_val = max(nums)
        
        for i in range(1,max_val+1):
            # print(i)
            if i not in nums:
                # print(i)
                return i
        # print(max_val+1  )
        return max_val+1 


    def firstMissingPositive_leetcode(self, nums):
        '''
        https://leetcode.com/problems/first-missing-positive/solutions/2550946/python-solution-100-explained/        '''
        
        # 看都看不懂
        # 這一步把列表裡面所有負數都改為0
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        # 

        for i in range(len(nums)):
            index = abs(nums[i])-1 
            if index<len(nums)and index>-1:
                if nums[index]==0:
                    nums[index]=-(len(nums)+1)
                else:
                    nums[index]=-1*abs(nums[index])
        for i in range(1,len(nums)+1):
            index = i -1 
            if nums[index]>=0:
                return i 
        return len(nums)+1







nums = [1,2,0]
# nums = [3,4,-1,1]
# nums = [7,8,9,12,11]
# nums = [2147483647]
nums = [-1,-2]

# obj = Solution().firstMissingPositive(nums)
obj = Solution().firstMissingPositive_leetcode(nums)


