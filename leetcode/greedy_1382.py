# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def balanceBST_leetcode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        v = []
        def dfs(node):
            if node:
                dfs(node.left)
                v.append(node.val)
                dfs(node.right)
        dfs(root)
        def bst(v):
            if not v:
                return None
            mid = len(v)//2
            root = TreeNode(v[mid])
            root.left = bst(v[:mid])
            root.right = bst(v[mid+1:])
            return root

        return bst(v)


root = [1,None,2,None,3,None,4,None,None]
obj = Solution().balanceBST_leetcode(root)