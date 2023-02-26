# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        二叉树中的最大路径和
        https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/3195903/beats-92-69-with-step-by-step-explanation/
        """
        def dfs(node):

            if not node:
                return 0  
            # 得到左边子树的最大和
            left_sum = max(dfs(node.left),0)
            # 同上
            right_sum = max(dfs(root.right),0)

            # 更新换代最大路径和
            self.max_path_sum = max(self.max_path_sum,node.val+left_sum,right_sum)

            # 返回当前节点的最大和及其节点的最大和
            #左右子树
            return node.val + max(left_sum,right_sum)
        # 初始化最长路径和
        self.max_path_sum = float('-inf')
        # 开始深度搜素
        dfs(root)
        return self.max_path_sum
    

'''上面说我超过回溯深度copy in case'''
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            # Base case: node is None
            if not node:
                return 0
            
            # Get the maximum sum of the left subtree
            left_sum = max(dfs(node.left), 0)
            # Get the maximum sum of the right subtree
            right_sum = max(dfs(node.right), 0)
            
            # Update the maximum path sum so far with the sum of the current node
            # and the maximum sums of the left and right subtrees
            self.max_path_sum = max(self.max_path_sum, node.val + left_sum + right_sum)
            
            # Return the maximum sum of the current node and the maximum sum of its
            # left and right subtrees
            return node.val + max(left_sum, right_sum)
        
        # Initialize the maximum path sum to negative infinity
        self.max_path_sum = float('-inf')
        
        # Start the depth-first search
        dfs(root)
        
        # Return the maximum path sum
        return self.max_path_sum
    

root = [1,2,3]
obj = Solution().maxPathSum(root)
