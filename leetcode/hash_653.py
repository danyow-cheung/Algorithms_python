# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        output = []

        self.inorder(root,output)
        l = 0
        r = len(output)-1
        while l<r:
            sum_val = output[l]+output[r]
            if sum_val==k:
                return True
            else:
                if sum_val>k:
                    r-=1
                else:
                    l+=1
        return False

    def inorder(self,root,output):
        '''二叉樹的前序遍歷'''
        if root==None:
            return
        else:
            self.inorder(root.left,output)
            output.append(root.val)
            self.inorder(root.right, output)

root = [5,3,6,2,4,None,7]
k = 9
obj = Solution().findTarget(root,k)