class MyQueue(object):
    '''使用棧實現隊列
    隊列：先進先出
    棧：先進後出

    '''
    def __init__(self):
        self.stack_in  =[]
        self.stack_out  =[]



    def push(self, x):
        """
        :type x: int
        :rtype: None
        将元素推到队列的末尾
        """
        self.stack_in.append(x)
        

    def pop(self):
        """
        :rtype: int
        從隊列的開頭移除並返回元素
        """

        # res = 0
        # while self.stack:
        #     res = self.stack.pop()
        # return res 

        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        返回隊列開頭的元素
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans 



        

    def empty(self):
        """
        :rtype: bool
        如果隊列為空，返回true
        """
        return not(self.stack_in or self.stack_out)


        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()