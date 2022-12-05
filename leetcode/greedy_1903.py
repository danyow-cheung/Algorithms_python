class Solution(object):
    def largestOddNumber_wrong_byme(self, num):
        """
        :type num: str
        :rtype: str
        """
        '''情况一：要先检查str中有没有奇数元素，如果没有直接返回"" '''
        num_lst = []
        ans = []
        # 统计str中有没有奇数的计数器
        count = 0
        for i in num:
            if not int(i)%2 == 0:
                count += 1
            num_lst.append(int(i))

        if count ==0:
            return ""



        '''情况二：先检查元素组成的整数是否是奇数，如果是直接返回原来的num'''
        # 返回本身已经是奇数的最大值

        if not int(num)%2==0:
            print('num is odd ')
            return  num

        '''情况三：在子序列中查找奇数，并收集到列表中，在列表中排序，使返回str的最大'''
        # 可以找最长子序列的情况是单元素列表中存在奇数
        for i in num_lst:
            if not i%2==0:
                ans.append(i)
        print(ans)

        return  str(max(ans))
    def largestOddNumber(self,num):
        '''learning by doing--leetcode'''
        # 倒序输出
        for j in range(len(num)-1,-1,-1):
            print(num[:j+1])

            if int(num[j])%2==1:
                return num[:j+1]

num = '52'
# num='4206'
num = "10133890"
obj = Solution().largestOddNumber(num)