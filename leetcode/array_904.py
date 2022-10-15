from asyncio import futures
from turtle import right


class Solution(object):
    def totalFruit_BruteForce(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        最长序列中只包含两个元素，就是元素值相同
        """
        max_len = 0 
        for i in range(len(fruits)):
            for j in range(i,len(fruits)):
                # 存储不同类别的集合
                basket = set()
                for curr in range(i,j+1):
                    # 存储下标
                    basket.add(fruits[curr])

                if len(basket)<=2:
                    max_len = max(max_len,j-i+1)

        return max_len

    def totalFruit_BruteForce_v2(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        最长序列中只包含两个元素，就是元素值相同
        暴力循环的优化版
        """
        max_len = 0 
        for left in range(len(fruits)):
            basket = set()
            right = left    
            while right<len(fruits):
                # 提前结束
                if fruits[right] not in basket and len(basket)==2:
                    break
                basket.add(fruits[right])
                right+=1 
            max_len = max(max_len,right - left)
        return max_len

    def totalFruit_SlidingWindow(self,fruits):
        """
        :type fruits: List[int]
        :rtype: int
        使用哈希表
        """
        basket = {}
        left = 0 
        for right,fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit,0)+1
            
            if len(basket)>2:
                basket[fruits[left]] -=1 
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1 
            # print(basket)
        return right-left+1 


nums = [1,2,1]
nums = [0,1,2,2]

obj = Solution().totalFruit_SlidingWindow(nums)