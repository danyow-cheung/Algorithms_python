class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        """首先需要從int中取出元素"""
        num = str(num)
        # 構造元素組成的列表
        nums = []
        for i in num:
            nums.append(i)


        '''在對元素進行貪心操作'''
        # 對數組進行排序，直接找最小兩位做為new1和new2的第一位數字
        nums.sort()

        '''貪心：找到sum（new1,new2）最小的值就返回'''
        # 初始化
        new1= [0]*2

        # 作為十位
        new1[0] += int(nums[0])*10
        new1[1] += int(nums[1])*10
        print(new1)

        for i in range(2,len(nums)-1):
            print(nums[i])
            new1[0]+= int(nums[i])
            new1[1]+= int(nums[i+1])
        print(new1)
        return sum(new1)

nums = 2932
nums = 4009
obj  = Solution().minimumSum(nums)