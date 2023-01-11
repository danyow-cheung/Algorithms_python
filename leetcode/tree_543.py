# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(root):
            if not root:
                return 0
            left = getDepth(root.left)
            right = getDepth(root.right)
            H = 1 + max(left,right)
            return H
        return getDepth(root)

    def diameterOfBinaryTree_leetcode(self,root):
        self.max_depth = 0
        self.getDepth(root)
        return  self.max_depth

    def getDepth(self,root):
        '''leetcode example'''
        if not root:
            return  0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        total = left+right

        self.max_depth = max(self.max_depth,total)
        return  max(left,right)+1


root = [1,2,3,4,5]
obj = Solution().diameterOfBinaryTree(root)