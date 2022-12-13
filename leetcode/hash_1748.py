import collections


class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        print(count)
        ans = 0
        for key,value in count.items():
            if value==1:
                ans += key
        print(ans)
nums =[1,2,3,2]
obj =Solution().sumOfUnique(nums)