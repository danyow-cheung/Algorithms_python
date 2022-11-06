class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        for i in operations:
            print(i)
            if i =="++X" or i=="X++":
                res += 1
            elif i =="--X" or i=="X--":
                res-=1
        print(res)
operations = ["--X","X++","X++"]
operations = ["++X","++X","X++"]
obj = Solution().finalValueAfterOperations(operations)