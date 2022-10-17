class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix,postfix=1,1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
            print(f"prefix={prefix}")
        print("----")
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
            print(f"postfix={postfix}")
        print(res)
        return res
            
original = [1,2,3,4]
obj = Solution().productExceptSelf(original)
