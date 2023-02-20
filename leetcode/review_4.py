class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        
        """
        nums1.extend(nums2)
        print(nums1)
        nums1.sort()
        # 二叉搜索的前提是元素是有排列顺序的
        if len(nums1)%2==0:# 偶数个
            a = len(nums1)/2 
            return float(nums1[a]+nums1[a-1])/float(2)


        else:
            a = len(nums1)/2 
            return float(nums1[a])




        
nums1 = [1,3]
nums2 = [2]
obj = Solution().findMedianSortedArrays(nums1, nums2)