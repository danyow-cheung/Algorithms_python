# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle_v1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow,fast = head.next,head.next.next
        while fast and fast.next and slow != fast:
            slow,fast = slow.next,fast.next.next
        if slow != fast:
            return None
        slow = head
        while slow!=fast:
            slow,fast = slow.next,fast.next
        return  slow

    def detectCycle_v2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow,fast = slow.next,head.next.next
            if slow==fast:
                break
        else:return None
        while head!=slow:
            head,slow = head.next,slow.next
        return head

    def detectCycle_v3(self, head):
        element_set = set()
        # curr = head
        while head:
            if head in element_set:
                return head
            element_set.add(head)
            head = head.next
        return None
head = [3,2,0,-4]
pos = 1
obj = Solution().detectCycle(head,pos)