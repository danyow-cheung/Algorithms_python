# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def inorder(o,c):
            if o:
                inorder(o.left,c.left)
                if o is target:
                    self.ans = c
                inorder(o.right,c.right)
        inorder(original,cloned)
        return self.ans

tree = [7,4,3,None,None,6,19]
target = 3
obj = Solution().getTargetCopy(tree,target)