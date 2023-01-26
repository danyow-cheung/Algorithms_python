class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        brute force
        """
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                # print(arr[i],arr[j])

                if arr[i]==2*arr[j] or 2*arr[i]==arr[j]:
                    print(arr[i],arr[j])

                    return True
        return False
        
arr = [10,2,5,3]
arr = [7,1,14,11]
obj = Solution().checkIfExist(arr)
