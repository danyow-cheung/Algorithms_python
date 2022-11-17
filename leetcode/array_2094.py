class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        需要找到所有不满足下述条件且互不相同的整数
        1. 该整数由digits中的三个元素按任意顺序依次连接组成
        2. 该整数不含前导零
        3. 该整数是一个偶数
        找出所有互不相同的整数按递增顺序排序，并以数组形式返回
        """
        res =[]

                

digits = [2,1,3,0]
obj = Solution().findEvenNumbers(digits)
