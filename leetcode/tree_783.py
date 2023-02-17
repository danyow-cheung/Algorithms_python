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
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)

        ans = float('inf')
        for i in range(len(res)-1):
            ans = min(ans,abs(res[i]-res[i+1]))
        # return abs(res[0]-res[1])
        return ans



root = [4,2,6,1,3]
obj = Solution().minDiffInBST(root)
