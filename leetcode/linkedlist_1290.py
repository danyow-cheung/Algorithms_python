# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        val = head.val
        # 當有下一步的時候
        while head.next:
            val = val*2 + head.next.val
            head = head.next 
        return val