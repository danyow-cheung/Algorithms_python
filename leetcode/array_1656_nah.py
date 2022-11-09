class OrderedStream(object):
    '''
    有 n 个 (id, value) 对，其中 id 是 1 到 n 之间的一个整数，value 是一个字符串。不存在 id 相同的两个 (id, value) 对。

    设计一个流，以 任意 顺序获取 n 个 (id, value) 对，并在多次调用时 按 id 递增的顺序 返回一些值。

    实现 OrderedStream 类：

    OrderedStream(int n) 构造一个能接收 n 个值的流，并将当前指针 ptr 设为 1 。
    String[] insert(int id, String value) 向流中存储新的 (id, value) 对。存储后：
    如果流存储有 id = ptr 的 (id, value) 对，则找出从 id = ptr 开始的 最长 id 连续递增序列 ，并 按顺序 返回与这些 id 关联的值的列表。然后，将 ptr 更新为最后那个  id + 1 。
    否则，返回一个空列表。

    '''
    def __init__(self, n):
        """
        :type n: int
        """
        # 当前指针为1
        self.ptr =1
        self.arr = [-1]*(n+1)
        self.n = n

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        res = []
        self.arr[idKey]=value
        while self.ptr<= self.n and self.arr[self.ptr]!=-1:
            res.append(self.arr[self.ptr])
            self.ptr+=1
        return res
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)