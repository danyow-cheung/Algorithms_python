# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        这道题目的本质是要比较两个树（这两个树是根节点的左右子树），
        遍历两棵树而且要比较内侧和外侧节点，
        所以准确的来说是
        【一个树的遍历顺序是左右中，一个树的遍历顺序是右左中】
        【递归】【递归】【递归】【递归】【递归】【递归】【递归】
        """
        def compare(left,right):
            if left is None and right is None:
                return True

            elif left is not None and right is None:
                return False

            elif left is None and right is not None:
                return  False

            # 排除了空节点的情况，再排除数值不相同的情况
            elif left.val != right.val:
                return False

            # 此时的情况是，左右节点不为空，且数值相同的情况
            outside = compare(left.left, right.left)
            inside = compare(left.right,right.right)
            isSame = outside and inside
            return isSame
        compare(p,q)


        # if not p and not q:
        #     '''头节点都没了，肯定True啊'''
        #     return True
        #
        # if p is None and q is not None:
        #     return False
        # elif p is not None and q is None:
        #     return False
        #
        # elif p.left is not None and q.left is not None:
        #     '''都存在左节点且值相同'''
        #     if p.left.val == q.left.val:
        #         return True
        #
        # elif p.right is not None and q.right is not None:
        #     '''都存在右节点且值相同'''
        #     if p.right.val == q.right.val:
        #         return True
        # else:
        #     return False
        #
