class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)==2:

            return sum(cost)
        cost.sort()
        ans = 0
        res = []
        print('倒序排序之后的数组',cost[::-1])
        for i in range(1,len(cost)+1):
            if len(res) ==2:
                # 保留结果
                ans += sum(res)
                # 清空列表
                # res.clear()
                del res[:]
                continue
            res.append(cost[-i])
            if cost[-i]>min(res):
                # 跳过这层循环
                continue
            print(res)
            # if res is not None:
        # res中还有元素
        if res:
            ans += sum(res)


        print(ans)
        return ans

cost = [1,2,3]
# cost = [6,5,7,9,2,2]
cost =[3,3,3,1]
obj = Solution().minimumCost(cost)