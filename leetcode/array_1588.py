class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        暴力解法+切片
        """
        n = len(arr)
        res = 0 
        # step =2 
        for l in range(1,n+1,2):
            for i in range(n-l+1):
                print(f"l = {l},i = {i},arr[i:i+l]={arr[i:i+l]}")
                res += sum(arr[i:i+l])
        return res 
        
arr = [1,4,2,5,3]
# arr = [1,2]
# arr= [10,11,12]
obj = Solution().sumOddLengthSubarrays(arr)