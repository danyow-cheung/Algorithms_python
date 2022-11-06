class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        - 找出数组1中没在数组2出现的元素
        - 找出数组2中没在数组1出现的元素
        """
        res = [[],[]]

        left = 0
        while left<len(nums1):
            if nums1[left] not in nums2 and nums1[left] not in res[0]:
                res[0].append(nums1[left])
            left+=1
        left = 0
        while left<len(nums2):
            if nums2[left] not in nums1 and nums2[left] not in res[1]:
                res[1].append(nums2[left])
            left+=1


        print(res)
nums1 = [1,2,3]
nums2 = [2,4,6]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

nums1 = [-68,-80,-19,-94,82,21,-43]
nums2 = [-63]
obj = Solution().findDifference(nums1,nums2)