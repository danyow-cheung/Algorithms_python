
class MyHashSet(object):

    def __init__(self):
        
        self.hash = {}
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            self.hash[key]+=1
        else:
            self.hash[key]=1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            del self.hash[key]

        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.hash:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)