import collections
from collections import  Counter
class Solution(object):
    def intersect_wa(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        应该满足小长度的数组寻找
        """
        # res = []
        # max_nums = []
        # if len(nums1)>=len(nums2):
        #     max_nums = nums1
        # else:
        #     max_nums = nums2
        # print(max_nums,nums2)


        # for x in nums1:
        #     if x in nums2:
        #         res.append(x)
        # print(res)

        a = [i for i in nums1 if i in nums2]
        b = [i for i in nums2 if i in nums1]
        print(min(a,b))

    def intersect_twopointers(self,nums1,nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        pt1 = 0
        pt2 = 0
        res = []
        while True:
            try:
                if nums1[pt1]>nums2[pt2]:
                    pt2+=1
                elif nums1[pt1]<nums2[pt2]:
                    pt1+=1
                else:
                    res.append(nums1[pt1])
                    pt1+=1
                    pt2+=1
            # 某一个数组到头了所以直接结束
            except IndexError:
                break
        print(res)

    def intersect_dictionary(self,nums1,nums2):
        counts = {}
        res = []
        for num in nums1:
            counts[num]=counts.get(num,0)+1

        for num in nums2:
            # 元素存在于nums1的字典里面
            if num in counts and counts[num]>0:
                res.append(num)
                counts[num]-=1
        print(res)

    def intersect_counter(self,nums1,nums2):
        counts = collections.Counter(nums1)
        res = []

        for i in nums2:
            if counts[i]>0:
                res.append(i)
                counts[i]-=1
        print(res)
nums1 = [1,2,2,1]
nums2 = [2,2]
nums2 = [2]
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
obj = Solution().intersect_counter(nums1,nums2)