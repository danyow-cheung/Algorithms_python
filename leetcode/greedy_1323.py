class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        最多更改一個數來獲得最大數字
        """
        # 已經是最大值，直接返回

        str_num = str(num)
        # print(num,type(num))
        # 構造元素組成的列表
        nums = []
        for i in str_num:
            nums.append(int(i))
        # 已經是最大值，直接返回
        # 排除沒有9的情況
        if 6 not in (nums):
            return num
        # 按照順序返回
        for i in range(len(nums)):

            if int(nums[i]) == 6:
                nums[i] = 9
                if self.cal_sum(nums) < num:
                    # 撤銷操作
                    nums[i] = 6
                else:
                    print(nums)
                    return self.cal_sum(nums)

            elif int(nums[i]) == 9:
                nums[i] = 6
                if self.cal_sum(nums) < num:
                    nums[i] = 9
                else:
                    print(nums)
                    return self.cal_sum(nums)

    def cal_sum(self, nums):
        res = ''
        for i in nums:
            res += str(i)
        # print(res)
        return int(res)