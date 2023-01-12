# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []

        def loop(node):

            if not node:
                return 0

            left = 0
            right = 0

            if node.left:
                left = node.left.val
            if node.right:
                right = node.right.val
            if node.right or node.left:
                if right != 0 and left != 0:
                    res.append(float(left + right) / 2)
                elif right != 0 and left == 0:
                    res.append(float(right))
                else:
                    res.append(float(left))

            loop(node.left)

            loop(node.right)

        res.append(root.val)
        loop(root)
        return res

    def averageOfLevels_leetcode(self,root):
        '''BFS'''
        queue = collections.deque([root])
        res =[]
        while queue:
            level_len = count = len(queue)
            level_sum = 0
            while count:
                node = queue.popleft()
                level_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count-=1
            res.append(float(level_sum)/level_len)
        return res


root = [3,9,20,None,None,15,7]
obj = Solution().averageOfLevels(root)