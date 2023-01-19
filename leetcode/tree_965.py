# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        testcase2:出錯
        """

        def bfs(node):
            if node:

                if node.left:
                    if node.left.val != node.val:
                        return False
                    bfs(node.left)

                if node.right:
                    if node.right.val != node.val:
                        return False
                    bfs(node.right)
                # if node.left.val!= node.val  or node.right.val != node.val:
                # return False
            return True

        return bfs(root)
    def isUnivalTree_leetcode(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(vals))==1

root = [1,1,1,1,1,None,1]
obj = Solution().isUnivalTree(root)