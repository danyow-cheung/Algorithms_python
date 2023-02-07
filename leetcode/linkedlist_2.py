# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        原始提交
        """
        # 虛擬頭節點》
        result = ListNode(0)
        result_tail = result 
        carry = 0 
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0 )
            val2 = (l2.val if l1 else 0 )
            carry,out = divmod(val1+val2+carry,10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return result.next 



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        自己寫的23.2.7但不通過，接下來看看別人怎麼寫的
        """
        res_1 = []
        res_2 = []
        while l1:
            res_1.append(str(l1.val))
            l1 = l1.next 
        while l2:
            res_2.append(str(l2.val))
            l2 = l2.next 
        val_1 = res_1[::-1]
        val_2 = res_2[::-1]
        res = int("".join(val_1))+int("".join(val_2))
        ans = str(res)[::-1]
        # print(val_1,val_2,type(res),res,ans,type(ans))
        '''RuntimeError:不是所需的返回數據結構'''
        return [int(i) for i in ans ]


    def addTwoNumbers(self,l1,l2):
        '''
        https://leetcode.com/problems/add-two-numbers/solutions/3153741/python-ez-code-using-a-loop-recursion-converting-linked-lists-explained/
        '''
        number1 = self.linked_list_number(l1)
        number2 = self.linked_list_number(l2)
        number = number1 + number2
        return self.number_to_linked_list(number)
    
    def linked_list_number(self,head):
        number = 0 
        multipler = 1 
        while head:
            number += head.val * multipler 
            multipler *= 10 
            head = head.next 
        return number 
    
    def number_to_linked_list(self,number):
        head = ListNode()
        current = head 
        while number>0:
            digit = number %10 
            current.next = ListNode(digit)
            current = current.next 
            number = number//10 
        
        if head.next:
            return head.next
        else:
            return head 
            


        
l1 = [2,4,3]
l2 = [5,6,4]
obj = Solution().addTwoNumbers(l1,l2)
