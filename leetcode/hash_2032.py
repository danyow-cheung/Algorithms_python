import collections


class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)

        # print(s1&s2,s1&s2,s2&s3)
        return (s1 & s2) | (s2 & s3) | (s1 & s3)

        

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
obj = Solution().twoOutOfThree(nums1,nums2,nums3)
