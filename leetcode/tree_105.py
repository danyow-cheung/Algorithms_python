# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree_leetcode(self, preorder, inorder):
        '''
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/2279180/python-explained/
        '''
        
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder,inorder[:INDEX])
            root.right = self.buildTree(preorder,inorder[INDEX+1:])
            return root 


    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        从前序与中序遍历构造二叉树
        """
        head = TreeNode(preorder[0])
        # print(head,head.val)
        left_node = []
        right_node = []
        # 捕获前序中间节点后面的

        # 捕获中序遍历前面的
        head_index = inorder.index(preorder[0])
        print(head_index)
        left_node.append(inorder[0:head_index])
        right_node.append(inorder[head_index+1:])

        print(left_node)
        print(right_node)

        
        
            


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
obj = Solution().buildTree(preorder,inorder)