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
                a = self.plus(dp[i])
                b = self.plus(nums[i:j+1])
                '''應該可以是實現的，但是報錯'''
                dp[i] = max(a,b)
                print("\n")
        print('final-dp',dp)


    def maxProduct_leetcode(self, nums):
        '''https://leetcode.com/problems/maximum-product-subarray/solutions/3091884/python-dynamic-programming-with-min-and-max-8-lines-86-ms-faster-than-80-77/'''
        mp = nums[0]
        ps = {nums[0]}
        for n in nums[1:]:
            if n==0:
                mp = max(mp,0)
                ps = {0}
            if n==1:
                mp = max(mp,1)

            ps = [p*n for p in ps]+[n]
            pmax ,pmin = max(ps),min(ps)
            mp,ps = max(mp,max),set([pmax,pmin])
        return mp 


    def maxProduct_leetcode_2(self,nums):
        '''https://leetcode.com/problems/maximum-product-subarray/solutions/2859129/python-js-easy-logic-kadane-s-algo-concise-solution-o-1-dp-o-n-tc/'''
        maxi = mini = res = nums[0]

        for num in nums[1:]:
            currMax = max(maxi * num, mini * num, num)
            currMin = min(maxi * num, mini * num, num)
            maxi = currMax
            mini = currMin
            res = max(res, maxi)
        
        return res

nums = [2,3,-2,4]
obj = Solution().maxProduct(nums)
# obj = Solution().maxProduct([1,1])
