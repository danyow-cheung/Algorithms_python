# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        可以通过测试但是没考虑到其他情况
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        # 当root有右值
        while root.right:
            res.append(root.right.val)
            root = root.right
        # 需要考虑的是【没有右边的但有左边的情况】 
        print(res)
        return res 

    def rightSideView_leetcode(self, root):
        ans = []
        def dfs(root,depth):
            if not root:
                return 
            if depth ==len(ans):
                # 首层
                ans.append(root.val)
            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
        dfs(root,0)
        return ans 
        

root = [1,2,3,None,5,None,4]
obj = Solution().rightSideView(root)