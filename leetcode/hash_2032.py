class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        ans = set()
        for i in nums1:
            ans.add(i)
        print('default set = ',ans)

        for i in nums3:
            if i not in ans:
                print(i)

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
obj = Solution().twoOutOfThree(nums1,nums2,nums3)
