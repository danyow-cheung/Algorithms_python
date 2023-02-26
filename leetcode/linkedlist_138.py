# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        https://leetcode.com/problems/copy-list-with-random-pointer/solutions/3205736/138-solution-with-step-by-step-explanation/
        """
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        # Create a new node with the same value as the original node
        node = Node(head.val,None,None)
        self.visited[head]=node 

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node 
    






head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
obj = Solution().copyRandomList(head)

