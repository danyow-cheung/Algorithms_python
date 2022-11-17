# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
            # 左子树上的左叶子
        left_left_sum = self.sumOfLeftLeaves(root.left)
        # 右子树上的左叶子
        right_left_sum = self.sumOfLeftLeaves(root.right)
        # 当前叶子数值
        cur_left_val = 0
        # 当前父节点有左节点且，该左节点是没有下一层左节点和右子节点
        # 即为所求
        if root.right and not root.left.left and not root.left.right:
            cur_left_val = root.left.val

        return cur_left_val + left_left_sum + right_left_sum

