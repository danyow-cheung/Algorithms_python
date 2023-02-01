# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: boola
        """
        res = []
        # 收集保存链表中的元素，再进行判断
        while head:
            res.append(head.val)
            head = head.next 
        return res == res[::-1]
 