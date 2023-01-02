# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def check(val,sum):
            if low <= root.val <=high:
                sum += root.val
            return sum
        sum=0
        if root:

            if root.left:
                sum = check(root.left.val,sum)
            sum = check(root.val,sum)
            if root.right:
                sum = check(root.right.val, sum)
        return sum

    def rangeSumBST_leetcode_iterative(self, root, low, high):
        ans = 0
        stack =[root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low<node.val:
                    stack.append(node.left)
                if node.val <high:
                    stack.append(node.right)
        return  ans

    def rangeSumBST_leetcode_recursive(self,root,low,high):
        def dfs(node):
            nonlocal ans
            if node:
                if low<=node.val<=high:
                    ans+=node.val
                if low<node.val:
                    dfs(node.left)
                if node.val<high:
                    dfs(node.right)
        ans = 0
        dfs(root)
        return  ans




root = [10,5,15,3,7,None,18]
low = 7
high = 15
obj = Solution().rangeSumBST(root,low,high)