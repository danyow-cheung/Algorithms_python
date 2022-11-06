class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(1,int(n/2)+1):
            print(i)
            if n%i == 0:
                print('n%i==0',i)
                if i+1==3:

                    print("find?")

n =2
n= 8
obj = Solution().isThree(n)