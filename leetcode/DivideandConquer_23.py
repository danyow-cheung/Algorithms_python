# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from queue import PriorityQueue # 優先隊列
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        將多個有順序的鏈表轉換為單個有順序的鏈表
        https://leetcode.com/problems/merge-k-sorted-lists/solutions/127466/merge-k-sorted-list/
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val,l))
        while not q.empty():
            val,node = q.get()
            point.next = ListNode(val)
            point = point.next 
            node = node.next 
            if node:
                q.put((node.val,node))
        return head.next 



    


lists = [[1,4,5],[1,3,4],[2,6]]
obj = Solution().mergeKLists(lists)