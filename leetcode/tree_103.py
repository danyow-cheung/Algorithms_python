# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
 
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        來回左右獲得值然後返回
        https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/solutions/2098804/python3-clean-solution-using-queue-level-order-traversal/
        """
        res = []
        if not root:
            return res 
        zigzag = True 
        q = collections.deque()
        q.append(root)
        while q:
            n = len(q)
            nodesofThisLevel = []
            for i in range(n):
                node = q.popleft()
                nodesofThisLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if zigzag:
                res.append(nodesofThisLevel)
                zigzag = False
            else:
                #反方向
                res.append(nodesofThisLevel[::-1])
                zigzag=True
        return res 
        


root = [3,9,20,None,None,15,7]
obj = Solution().zigzagLevelOrder(root)