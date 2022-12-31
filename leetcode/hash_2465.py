class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res =set()
        nums.sort()
        while len(nums)!=0:
            print('nums=',nums)

            avg = (nums[-1]+nums[0])/2
            res.add(avg)
            nums.remove(nums[-1])
            nums.remove(nums[0])

        print(res)
        return  len(res)

    def leetcode(self,nums):
        nums.sort()
        n, u = len(nums), set()

        for i in range(0, n // 2):
            u.add((nums[i] + nums[n - i - 1]) / 2)

        return len(u)

nums = [4,1,4,0,3,5]
nums = [9,5,7,8,7,9,8,2,0,7]
obj = Solution().distinctAverages(nums)