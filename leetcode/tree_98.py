# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        stack = [None]

        prev = -float("inf")
        while stack:
            while root:
                stack.append(root)
                root = root.left
            x = stack.pop()
            if x:
                if x.val <= prev:
                    return False
                prev = x.val
                root = x.right

        return True
