# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList_leetcode(self,head):
        '''need two pointers head and tail to support operations at both ends
        變量
        - head 頭指針
        - odd  尾指針
        - evenhead 頭指針 (另外一個鏈表)
        - even  尾指針(另外一個鏈表)
        '''
        odd = ListNode(0)
        even = ListNode(0)
        oddhead = odd 
        evenhead= even 
        isOdd = True 

        while head:
            if isOdd:
                # 虛擬頭節點
                odd.next = head 
                odd = odd.next 
            else:
                even.next = head 
                even = even.next 
            isOdd = not isOdd 
            head = head.next 
        even.next= None
        odd.next = evenhead.next 
        return (oddhead.next)

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res =[]
        if not head:
            return head 
        last = None
        while head.next:
            head = head.next 
        last = head.val 
        print(last)
        while head.next:
            res.append(head.val)
            head = head.next.next
            if head.next: 
                res.insert(len(res),head.next.val)
        # 最後一位的
        res.append(head.val)
        print(head,res)

head = [1,2,3,4,5]
# obj = Solution().oddEvenList(head)
obj = Solution().oddEvenList_leetcode(head)