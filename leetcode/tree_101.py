# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        递归 后序遍历
        """
        if not root:
            return True

        def compare(left, right):
            if left is not None and right is None:
                return False
            elif left is None and right is not None:
                return False
            elif right is None and left is None:
                return True
            elif right.val != left.val:
                return False
                # 比较外侧节点是否对称
            outside = compare(left.left, right.right)
            # 比较内侧节点是否对称
            inside = compare(left.right, right.left)
            res = outside and inside
            return res

        return compare(root.left, root.right)
