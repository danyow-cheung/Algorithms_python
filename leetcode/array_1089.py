class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # right = len(arr)-1
        n_len = len(arr)
        i = 0
        j = len(arr)
        while i < j:
            if arr[i]==0:
                arr.insert(i+1,0)
                i+=1
            i+=1
        print(arr[:])
        arr[:] = arr[:n_len]
        print(arr[:])

arr =[1,0,2,3,0,4,5,0]
obj = Solution().duplicateZeros(arr)
