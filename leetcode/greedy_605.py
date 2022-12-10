class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        left = 0

        while left<len(flowerbed):
            print(left,n,flowerbed[left])

            # 往后面看1位
            if flowerbed[left]==1:
                left+=2
            n-=1
            flowerbed[left]=1
            left+=2


        print(flowerbed)
        print(n)


flowerbed = [1,0,0,0,1]
n=2

flowerbed = [1,0,0,0,1,0,1]
n =1

object = Solution().canPlaceFlowers(flowerbed,n)