class Solution(object):
    def arrayPlus(self,nums):
        '''数组转换为乘'''
        if not nums:
            return 1
        res = 1 
        for i in nums:
            res*=i 
        return res 

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        超时
        """
        res = []
        for i in range(len(nums)):
            print(nums[i],nums[:i],nums[i+1:])
            count = self.arrayPlus(nums[:i])*self.arrayPlus(nums[i+1:])
            res.append(count)
        print(res)
    def productExceptSelf_leetcode(self,nums):
        '''
        https://leetcode.com/problems/product-of-array-except-self/solutions/2846283/python-96-15-faster-t-c-o-n-s-c-o-1-prefix-and-postfix-array/
        '''
        prefix,n=1,len(nums)
        answer=[1]
        for i in range(1,n):
            prefix*=nums[i-1]
            answer.append(prefix)
        postfix=1
        for i in range(n-2,-1,-1):
            # print(nums[i],nums[i+1])
            postfix*=nums[i+1]
            answer[i]*=postfix
        return answer


nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
# obj = Solution().productExceptSelf(nums)
obj = Solution().productExceptSelf_leetcode(nums)
