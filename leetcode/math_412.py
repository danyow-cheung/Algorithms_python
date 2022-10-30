class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        
        for i in range(1,n+1):
            print(i)
            
            if i %3 == 0 and i %5==0 :
                res.append("FizzBuzz")

            elif i%3==0:
                res.append("Fizz")
            elif i%5==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res 
n = 3
obj = Solution().fizzBuzz(n)
