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
    
    def findMedianSortedArray_leetcode(self,nums1,nums2):
        '''https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2934686/simple-python-solution-using-functions/'''
        # 將nums2添加到nums1 
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:# 偶數長度
            a = len(nums1)/2 
            # 返回中間元素和上一個元素的和
            return float(nums1[a]+nums1[a-1])/float(2)
        else:
            a = len(nums1)/2 
            return float(nums1[a])
    
    def findMedianSortedArray_leetcode2(self,nums1,nums2):
        '''
        https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2953739/python-solution-using-basics/
        '''
        list3 = nums1 + nums2
        list3.sort()
        len = len(list3)
        if len%2==0:
            r = list3((len/2)-1)+list3((len/2))
            return r*0.5 
        else:
            return list3((len-1)/2)
            
nums1 = [1,3] 
nums2 = [2]
nums1 = [1,2] 
nums2 = [3,4]

obj = Solution().findMedianSortedArrays(nums1,nums2)