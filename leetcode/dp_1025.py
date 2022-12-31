class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count =0
        for i in range(1,n):

            if n%i==0:
                print('x',i)
                n = n-i
                count+=1
        if count%2==0:
            return False
        return True

    def divisorGame_leetcode(self,n):
        '''数学式的解答方法
        有解释，但是不想看
        https://leetcode.com/problems/divisor-game/solutions/274606/java-c-python-return-n-2-0/
        '''
        return n%2==0




n = 3
obj = Solution().divisorGame(n)