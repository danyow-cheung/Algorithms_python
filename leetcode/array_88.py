class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 特殊情况是nums2为空
        if nums2 is None or n ==0:return nums1
        # nums2的指针
        left = 0 
        while m < len(nums1) and left < n:
            nums1[m]=nums2[left]
            left+=1
            m+=1 
        nums1.sort()
        print(nums1) 

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
nums1 = [1]
m = 1
nums2 = []
n = 0


obj = Solution().merge(nums1,m,nums2,n)