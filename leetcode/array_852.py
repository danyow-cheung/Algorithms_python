class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr)<3:
            print("wrong length of array")
            exit(0)
        left = 0 
        right = len(arr)-1

        
        while left<right:
            middle = (left+right)//2 
            print(arr[middle])
            if arr[middle]>arr[left]:
                left+=1 
            if arr[middle]>arr[right]:
                right-=1 
             
        print(f"left = {left},right={right}")

    def peakIndexInMountainArray_official_linear(self, arr):
        # 思路是山脉会一直增大直到减少，这样就会得出下标
        for i in range(len(arr)):
            if arr[i]>arr[i+1]:
                return i 
    def peakIndexInMountainArray_official_binary_search(self, arr):
        left = 0 
        right = len(arr)-1 
        while left<right:
            mi = (left+right)/2 
            # 这一步的思路等同于～linear步骤
            if arr[mi]<arr[mi+1]:
                left=mi+1 
            else:
                right = mi
        return left

    
arr = [0,2,1,0]
arr = [0,10,5,2]
arr=[0,1,0]
obj = Solution().peakIndexInMountainArray(arr)
