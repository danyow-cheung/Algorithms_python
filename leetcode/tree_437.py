# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum_bruteForce(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # head = root

        self.res = 0
        self.dfs(root,targetSum)
        return self.res 

    def dfs(self,node,target):
        if node is None:
            return
        self.test(node,target)
        self.dfs(node.left,target)        
        self.dfs(node.right,target)
    
    def test(self,node,target):
        if node is None:
            return 
        if node.val == target:
            self.res+=1 
        self.test(node.left,target-node.val)
        self.test(node.right,target-node.val)
        

root = [10,5,-3,3,2,None,11,3,-2,None,1]
targetSum = 8
# Output: 3

obj = Solution().pathSum_bruteForce(root,targetSum)
