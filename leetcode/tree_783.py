# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def dfs(root):
            if not root:
                return 
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        res.sort()
        print(res)
        


root = [4,2,6,1,3]
obj = Solution().minDiffInBST(root)
