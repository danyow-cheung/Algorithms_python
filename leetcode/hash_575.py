class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        num = len(candyType)//2
        candy = set(candyType)
        print(candy,num)
        if num<=len(candy):
            return  num
        else:
            return  len(candy)



candyType =[1,1,2,2,3,3]
candyType = [1,1,2,3]
candyType = [1,1,1,1]
obj =Solution().distributeCandies(candyType)