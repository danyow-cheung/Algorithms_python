# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/2982456/python3-simple-bfs/
        """
        if not root:
            return
        result,curr_level = [[root.val]],[root]
        while curr_level:
            next_level = []
            vals = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    vals.append(node.right.val)
            if next_level:
                # curr_level = next_level.copy()
                curr_level = next_level[:]

                result.append(vals)
            else:
                break
        return result

root = [3,9,20,None,None,15,7]
obj = Solution().levelOrder(root)