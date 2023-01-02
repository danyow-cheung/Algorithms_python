# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        target = root.val

        if root:
            if root.left:
                target -= root.left.val
            if root.right:
                target-=root.right.val
        return target==0

root = [10,4,6]
obj = Solution().checkTree(root)