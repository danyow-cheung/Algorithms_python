# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ans = []
        count = collections.Counter()
        def encode(root):
            if not root:
                return ''
            encoded = str(root.val)+'#'+encode(root.left)+'#'+encode(root.right)
            count[encoded]+=1 
            if count[encoded]==2:
                ans.append(root)
            return encoded
        encode(root)
        return ans 
        

root = [1,2,3,4,None,2,4,None,None,4]
obj = Solution().findDuplicateSubtrees(root)