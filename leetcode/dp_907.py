class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp = [[]  for _ in range(len(arr))]
        res = 0 
        for i in range(len(arr)):
            min_val = 0
            for j in range(i,len(arr)):
                min_val = min(arr[i:j+1])
                print(arr[i:j+1],min_val)
                res += min_val 

        print('res',res)
    '''
    https://leetcode.com/problems/sum-of-subarray-minimums/solutions/2700011/sum-of-subarray-minimums/
    '''
    def sumSubarrayMins_leetcode(self, arr):
        MOD = 10**9+7 
        stack = []
        sum_of_minimums = 0
        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]] >=arr[i]):
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i 

                count = (mid-left_boundary)*(right_boundary-mid)
                sum_of_minimums += (count*arr[mid])
            stack.append(i)
        return sum_of_minimums % MOD
        


arr = [3,1,2,4]
arr = [11,81,94,43,3]

obj = Solution().sumSubarrayMins(arr)