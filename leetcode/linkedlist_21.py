# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        seek,target  = (list1,list2) if list1.val < list2.val else (list2,list1)
        print(seek,target)

        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next,target = target,seek.next
            seek = seek.next

        return head

list1 = [1,2,4]
list2 = [1,3,4]
obj = Solution().mergeTwoLists(list1,list2)