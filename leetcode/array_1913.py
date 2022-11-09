class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        两个数对之间的最大乘积差
        两个数对 (a, b) 和 (c, d) 之间的 乘积差 定义为 (a * b) - (c * d) 。
        例如，(5, 6) 和 (2, 7) 之间的乘积差是 (5 * 6) - (2 * 7) = 16 。
        给你一个整数数组 nums ，选出四个 不同的 下标 w、x、y 和 z ，使数对 (nums[w], nums[x]) 和 (nums[y], nums[z]) 之间的 乘积差 取到 最大值 。

        返回以这种方式取得的乘积差中的 最大值 。

        """
        # 找到数据中最大的两个值和最小的两个值，然后做公式

        sorted_num = sorted(nums)
        print(sorted_num)

        # 后两位最大值
        max_val = sorted_num[-2:]
        # 前两位最小值
        min_val = sorted_num[:2]
        # print(max_val,min_val)
        # max_val= [res*=i for i in max_val res =0]
        max_res = 1
        for i in max_val:
            max_res*=i
        min_res = 1
        for i in min_val:
            min_res *= i
        print(max_res-min_res)
    def maxProductDifference_leetcode(self,nums):
        nums.sort(reverse=True)
        return nums[0]*nums[1]-nums[-1]*nums[-2]

nums = [5,6,2,7,4]
obj = Solution().maxProductDifference(nums)