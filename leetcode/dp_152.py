from functools import reduce

class Solution(object):
    def plus(self,myList):
        
        # res = 1 
        if not myList:
            return -1 

        # for i in range(len(lst)):
        #     res *= lst[i] 
        # print(res)

        # return res 
        result = 1
        for x in myList:
            result = result * x  
        return result  


    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[-1] for i in range(len(nums))]
        # print(dp)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                # print(nums[i],nums[j])
                # print(dp,type(dp[i]),dp[i])
                # print(nums[i:j+1])
                # print(dp[i],type(dp[i]))
                # dp[i] = max(self.plus(dp[i]),self.plus(nums[i:j+1]))
                a = self.plus(dp[i])
                b = self.plus(nums[i:j+1])
                # a = reduce(lambda x,y:x*y ,dp[i])
                # b = reduce(lambda x,y:x*y ,nums[i:j+1])
                
                # print(dp[i],type(dp[i]))
                # print(nums[i:j+1],type(nums[i:j+1]))
                # dp[i] = max(self.plus(dp[i]),self.plus(nums[i:j+1]))
                dp[i] = max(a,b)
                print("\n")

        print('final-dp',dp)


nums = [2,3,-2,4]
obj = Solution().maxProduct(nums)
# obj = Solution().maxProduct([1,1])
