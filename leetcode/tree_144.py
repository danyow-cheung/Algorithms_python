# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def loop_traversals(root):
            if root == None:
                return
            res.append(root.val)
            loop_traversals(root.left)
            loop_traversals(root.right)

        loop_traversals(root)
        return res
