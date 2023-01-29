# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        # 直接在root1上进行操作
        if  root1 and root2:
            # 位置相同的區域直接互相添加數字
            root = TreeNode(root1.val + root2.val) # 中
            root.left = self.mergeTrees(root1.left, root2.left) #左
            root.right = self.mergeTrees(root1.right, root2.right) # 右

            return root
        else:
            return root1 or root2
    