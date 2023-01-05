"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''Thx to https://leetcode.com/problems/n-ary-tree-postorder-traversal/solutions/155806/python-iterative-and-recursive-solution-with-explanation/'''
class Solution(object):
    def postorder_recursion(self, root):
        """
        :type root: Node
        :rtype: List[int]
        N叉树的后续遍历--左右中,递归遍历
        """
        res =[]
        if root ==None:
            return res
        def recursion(root,res):
            for child in root.children:
                recursion(child,res)
            res.append(root.val)
        recursion(root,res)
        return res


    def postorder_iteration(self, root):
        # Iteration is basically pre-order traversal but rather than go left, go right first then reverse its result.
        res = []
        if root ==None:
            return  res
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)
        return res[::-1]


root = [1,None,3,2,4,None,5,6]
obj = Solution().postorder(root)