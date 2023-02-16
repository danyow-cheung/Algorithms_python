class Solution(object):
    def calculate_leetcode_true(self,s):
        '''
        https://leetcode.com/problems/basic-calculator-ii/solutions/2531928/python-stack/
        '''
        pass 
    
    def calculate_leetcode_false(self, s):
        '''
        无效
        https://leetcode.com/problems/basic-calculator-ii/solutions/63076/python-short-solution-with-stack/
        '''
        op = "+"
        val = 0 
        stack = []
        for i,x in enumerate(s):
            if x.isdigit():
                val = 10 * val + int(x)
            if x in '+-*/' or i ==len(s)-1:
                if op=='+':
                    stack.append(val)
                elif op=='-':
                    stack.append(-val)
                elif op=='*':
                    stack.append(stack.pop()*val)
                elif op=='/':
                    stack.append(int(stack.pop()/val))
                op = x 
                val = 0 
        return sum(stack)




    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        for i in range(len(s)):
            # print(i)
            if  i == "*":
                last = res.pop()
                i = last * s[i+1]
            elif i=='/':
                last = res.pop()
                i = last / s[i+1]

            # res.append(i)
        print(res)



s = "3+2*2"
obj = Solution().calculate(s)