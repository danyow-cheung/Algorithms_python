
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root 
        stack = [root]
        for i in range(3):
            
            print(stack.pop())
        res = []
        # while root:
            
        #     res.append(root.val)

        #     if not root.right :
        #         stack.append('#')
        # # print(root.val,root.left,root.right)

    def connect_leetcode(self, root):
        head = root 
        while root:
            cur,root = root,root.left 
            while cur:
                if cur.left:
                    cur.left.next = cur.right 
                    if cur.next:
                        cur.right.next= cur.next.left 
                else:
                    break
                cur = cur.next 
        return head 
        
root = [1,2,3,4,5,6,7]
obj = Solution().connect(root)