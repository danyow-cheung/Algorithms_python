# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        https://leetcode.com/problems/reverse-linked-list/solutions/3011853/o-n-solution-with-step-by-step-visualization-video/

        """
        new_lst = None
        current = head
        while current:
            next_node = current.next
            current.next = new_lst
            new_lst = current
            current = next_node
        return  new_lst


head = [1,2,3,4,5]
obj = Solution().reverseList(head)