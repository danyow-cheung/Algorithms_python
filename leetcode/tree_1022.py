# Definition for a binary tree node.
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solutions/797205/sum-root-to-leaf-binary-numbers/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf_v1(self, root):
        '''Iterative Preorder Traversal'''
        root_to_leaf = 0
        stack = [(root,0)]
        while stack:
            root,curr_number = stack.pop()
            # print(root,curr_number)
            if root is not None:
                curr_number = (curr_number<<1)|root.val
                # if it's a leaf,update root-to-leaf sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.right,curr_number))
                    stack.append((root.left,curr_number))
        return root_to_leaf

    def sumRootToLeaf_v2(self, root):
        '''Recursive preorder traversal'''
        def preorder(r,curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number<<1)|r.val
                # if it's a leaf,update root-to-leaf sum
                if not(r.left or r.right):
                    root_to_leaf += curr_number
                preorder(r.left,curr_number)
                preorder(r.right,curr_number)
        root_to_leaf = 0
        preorder(root,0)
        return  root_to_leaf
    def sumRootToLeaf_v3(self, root):
        '''Morris Preorder Traversal'''
        root_to_leaf = curr_number = 0
        while root:

            # if there is a left  child
            # then compute the predecessor
            # if there is no link predecessor.right = root -> set it
            # if there is a link predecessor.right = root -> break it
            if root.left:
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps+=1

                # set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = (curr_number<<1)|root.val
                    predecessor.right = root
                    root = root.left
                # break the link predecessor.right = root
                # once the link is broken
                # it's time to change subtree and go to the right
                else:
                    # if you are on the leaf,update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # this part of tree is explored,backtrack
                    for _ in range(steps):
                        curr_number>>=1
                    predecessor.right = None
                    root = root.right

            # if there is no left child
            # then just go right
            else:
                curr_number = (curr_number<<1)|root.val
                # if you are on the leaf,update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right
        return  root_to_leaf




root = [1, 0, 1, 0, 1, 0, 1]
obj = Solution().sumRootToLeaf_v1(root)