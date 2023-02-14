class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float('inf')


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append((val,self.min))
        self.min = min(self.min,val)

    def pop(self):
        """
        :rtype: None
        """
        
        self.min = self.stack[-1][-1]
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        # 得到輚頂元素
        return self.stack[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()