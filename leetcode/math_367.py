import numbers


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，
        否则返回 false 。
        进阶：不要 使用任何内置的库函数，如  sqrt 。
        【需要用到二叉树搜索】算法知识，还没学到so
        """
        n = 0 
        while n*n <= num:
            n+=1
        sqrt= n-1 
        print(sqrt)
        
        if sqrt*sqrt == num:
            return True 
        else:
            return False 

number = 16
number = 9
obj = Solution().isPerfectSquare(number)
        