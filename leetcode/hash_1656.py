class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ptr =1
        self.hash = [""]*(n+1)

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.hash[idKey] = value

        res = []
        if idKey == self.ptr:
            while self.ptr<len(self.hash) and self.hash[self.ptr]:
                res.append(self.hash[self.ptr])
                self.ptr+=1
        return res



# Your OrderedStream object will be instantiated and called as such:
n = 5
obj = OrderedStream(n)
param_1 = obj.insert(5,None)
param_1 = obj.insert(3,'ccccc')
param_1 = obj.insert(1,'aaaaa')
param_1 = obj.insert(2,'bbbbb')
param_1 = obj.insert(5,'eeeee')
param_1 = obj.insert(4,'ddddd')