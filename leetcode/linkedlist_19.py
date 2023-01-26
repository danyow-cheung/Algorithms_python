# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head 
        count =0 
        while cur != None:
            count += 1
            cur = cur.next 
        
        # 刪除元素對應的索引
        idx = count - n 
        if count==n:
            return head.next 
        cur = head 
        for i in range(1,idx):
            cur = cur.next 
        cur.next = cur.next.next 
        return head 
        