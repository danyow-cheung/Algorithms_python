# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode_navie(self, head):
        '''go through the linked list once to find its length'''
        '''go through it again but only half way'''
        res = head
        l = 0
        while head:
            head = head.next
            l+=1
        mid = l//2
        while mid:
            res = res.next
            mid -= 1
        return  res

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow,fast = head
        while fast and fast.next:
            slow = slow.fast
            fast = fast.next.next
        return slow


head = [1,2,3,4,5]
obj = Solution().middleNode(head)