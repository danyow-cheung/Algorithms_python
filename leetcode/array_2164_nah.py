class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res_even = []
        res_odd = []
        # for i in range(len(nums)):
        #     if nums[i]%2==0:
        #         res.insert(i,nums[i])
        #     if nums[i]%2!=0:
        #         print("3",nums[i])
        #         res.insert(i,nums[i])
        # print(res)
        left = 0 
        while left < len(nums):
            if nums[left]%2==0:
                res_even.append(left) 
            if nums[left]%2!=0:
                res_odd.append(left)
            left+=1

        print(res_even,res_odd)
        
nums = [4,1,2,3]
obj = Solution().sortEvenOdd(nums)