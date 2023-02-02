# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList_leetcode(self, head):
        '''
        https://leetcode.com/problems/sort-list/solutions/3052136/python-iterate-all-sort-and-reconstruct-the-list/
        '''
        if not head :return

        node = head 
        l = [[head.val,head]]
        while node.next:
            node = node.next 
            l.append([node.val,node])
        
        l.sort(key=lambda x:x[0])
        
        # reconstruct the list 
        node = head = l[0][1]
        for k,v in l[1:]:
            node.next = v 
            node = node.next 
        node.next =None
        return head  


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head 
        res = []
        while head.next:
            res.append(head.val)
        print(res)
        return res.sort()