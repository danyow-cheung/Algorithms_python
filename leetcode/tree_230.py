# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        OMG我自己写的没看一点参考呢
        """
        
        def dfs(node,res):
            if not node:
                return 
            res.append(node.val)
            dfs(node.left,res)
            dfs(node.right,res)
            return res 
        res = dfs(root,[])
        res.sort()
        return res[k-1]



root = [3,1,4,None,2]
k = 1
obj = Solution().kthSmallest(root,k)