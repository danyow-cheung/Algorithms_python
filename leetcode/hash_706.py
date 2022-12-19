class MyHashMap(object):

    def __init__(self):
        self.hash = {}

    def contains(self,key):
        if key in self.hash:
            return True
        return False

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.contains(key):
            self.hash.update({key:value})
        else:
            self.hash[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.contains(key):
            return self.hash[key]
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            del self.hash[key]


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()

key = 1
value =2

obj.put(key,value)
exit(0)

param_2 = obj.get(key)
obj.remove(key)
