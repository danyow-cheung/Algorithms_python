class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        给你一个下标从 0 开始的整数数组 nums 。在一步操作中，你可以执行以下步骤：

            从 nums 选出 两个 相等的 整数
            从 nums 中移除这两个整数，形成一个 数对
        请你在 nums 上多次执行此操作直到无法继续执行。

        返回一个下标从 0 开始、长度为 2 的整数数组 answer 作为答案，
        其中 answer[0] 是形成的数对数目
        ，answer[1] 是对 nums 尽可能执行上述操作后剩下的整数数目。
        """
        # 删去的数目
        count = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                # print(nums[i],nums[j])
                if nums[i]==nums[j]:
                    # 还需要删除元素
                    count += 1


        # 剩下元素的数目
        left = len(nums) - count*2
        print(count,left)


    def numberOfPairs_leetcode(self,nums):
        from collections import  Counter
        c = Counter(nums)
        re_count = 0
        count = 0
        for key,value in c.items():
            print(key,value)
            count += value//2
            re_count += value%2

        return [count,re_count]

nums = [1,3,2,1,3,2,2]
obj = Solution().numberOfPairs_leetcode(nums)