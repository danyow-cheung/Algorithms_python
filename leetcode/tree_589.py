# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder_leetcode(self,root):
        if not root:
            return
        vals = []
        l = [root]
        while l:
            node = l.pop(0)
            vals.append(node.val)
            l = node.children+l
        return vals

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        前序遍歷，中左右
        """
        res = []
        def bfs(node):
            if node:
                res.append(node.val)
                bfs(node.children)
        root = Node(root)

        bfs(root)
        print(res)

        return  res

root = [1,None,3,2,4,None,5,6]
obj = Solution().preorder(root)