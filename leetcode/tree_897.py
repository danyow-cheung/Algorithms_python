# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST_v1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Get the in order list of the tree,and generate the new tree
        """
        def sortBST(node):
            if not  node:
                return []
            # return the in order BST nodes in list
            return sortBST(node.left)+[node.val]+sortBST(node.right)

        # the in order sorted list of the trees nodes
        sorted_lst = sortBST(root)
        # generate new tree:temp for update,ans for return root
        ans = temp = TreeNode(sorted_lst[0])
        # insert nodes to the right side of the new tree
        for i in range(1,len(sorted_lst)):
            temp.right = TreeNode(sorted_lst[i])
            temp = temp.right
        return ans


    def increasingBST_v2(self, root):
        '''Track the old tree in order and generate the new tree at the same time'''
        ans = self.cur  = TreeNode()
        def inorder(node):
            if node:
                # track the left side first
                inorder(node.left)

                # update the new tree
                self.cur.right = TreeNode(node.val)
                self.cur = self.cur.right
                # track the right side then
                inorder(node.right)
        inorder(root)
        return  ans.right


root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
obj = Solution().increasingBST_v1(root)