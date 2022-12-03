import collections


class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        第一次移动保持元素的奇偶性不变。
        第二次移动会更改元素的奇偶性。
        因为第一次移动是无消耗的，如果所有元素都有一样的奇偶性，答案是0
        找到最小花费为了所有元素有一样的奇偶性
        """
        '''构建一个哈希表
        key：元素下标
        val：元素数量
        '''
        def check_even(num):
            # 检查是否是否为偶数
            if num %2==0:
                return True
            else:
                return False

        count = collections.Counter(position)

        print(count)
        cost = 0
        even = 0
        # print(count.most_common(1))
        max_val = max(count,key=count.get)
        print(max_val)
        for key,value in count.items():

            # 先从出现次数多的选择
            if key == max_val:
                even = key
            else:
                cost= (key-even)*value
        print(cost)
        return cost
    def minCostToMoveChips_leetcode(self,position):
        nOdd, nEven = 0, 0
        for i in position:
            if i % 2 == 0:
                nEven += 1
            else:
                nOdd += 1
        return min(nEven, nOdd)

position = [1,2,3]

position = [2,2,2,3,3]
# position = [1,1000000000]
position = [2,3,3]
obj = Solution().minCostToMoveChips(position)