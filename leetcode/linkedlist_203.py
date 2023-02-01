# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # if not head:
            # return head 
        '''在链表上添加一个虚拟头节点'''
        dummy = ListNode(next= head )
        cur = dummy
        while (cur.next!=None): # 當當前節點不是最後一位的時候
            if (cur.next.val==val):# 找到要刪除的節點
                cur.next = cur.next.next
            else:
                cur = cur.next # 繼續查找下一個元素
        return dummy.next 
        