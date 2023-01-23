class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        diff = arr[1]-arr[0]
        for i in range(len(arr)-1):
            # print(arr[i])
            if arr[i+1]-arr[i]!=diff:
                return False
        return True
        

arr = [3,5,1]
obj  = Solution().canMakeArithmeticProgression(arr)