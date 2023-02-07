# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''感謝好大姊
https://leetcode.com/problems/binary-search-tree-iterator/solutions/52642/two-python-solutions-stack-and-generator/?envType=study-plan&id=level-2&languageTags=python
'''
class BSTIterator_stack(object):
    '''使用輚來實現'''
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left 

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        x = node.right 
        while x:
            self.stack.append(x)
            x = x.left 
        return node.val 
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)>0


class BSTIterator_generator(object):
    '''使用生產器'''
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.last = root 
        while self.last and self.last.right:
            self.last = self.last.right 
        self.current = None
        self.g = self.iterate(root)

        

    def next(self):
        """
        :rtype: int
        """
        return next(self.g)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current is not self.last

    def iterate(self,node):
        
        if node is None:
            return
        
        for x in self.iterate(node.left):
            yield x 
        self.current = node 
        
        yield node.val 
        
        for x in self.iterate(node.right):
            yield x 
        

root = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]


# Your BSTIterator object will be instantiated and called as such:

obj = BSTIterator_stack(root)
param_1 = obj.next()
param_2 = obj.hasNext()
