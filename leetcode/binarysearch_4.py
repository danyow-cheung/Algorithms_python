class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # print(nums1)

        mid = (len(nums1)+len(nums2))//2
        print(mid)
        
nums1 = [1,3] 
nums2 = [2]
nums1 = [1,2] 
nums2 = [3,4]

obj = Solution().findMedianSortedArrays(nums1,nums2)