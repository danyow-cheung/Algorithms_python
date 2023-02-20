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
        """
        # res = ListNode()
        res = []
        head_1 = ListNode(l1)
        head_2 = ListNode(l2)

        # while head_1.next and head_2.next:
        for i ,j in zip(head_1.val,head_2.val): # 這樣寫的話受鏈表長度影響 -> 應該用if l1.val else 0 的形式
            print('i-j',i,j)
            res.append(i+j)
        print(res)
        for i in range(len(res)-1):
            if res[i]>=10:
                res[i] = res[i]//10 
                res[i+1]+=1 
        print(res)

        return ListNode(res)
        
    def addTwoNumbers_v2(self, l1, l2):
        '''
        https://leetcode.com/problems/add-two-numbers/solutions/127833/add-two-numbers/
        '''
        print('--------v2--------')
        # 虛擬頭節點,初始化鏈表頭節點
        res = ListNode(0)
        curr = res 
        carry = 0 # 設置是否累加0 的標兵文件

        while l1!=None  or l2!=None or carry!=0:        #適用於兩個鏈表不同長度或者是長度最後但是還要累加1的情況
            
            l1_val =  l1.val if l1 else 0 
            l2_val  =  l2.val if l2 else 0

            curSum = l1_val+l2_val+carry 
            carry = curSum//10 # 判斷是否大於10
            # 初始化下一個新節點來組成鏈表
            newnode = ListNode(curSum%10)   # 18%10 =8 多出多少新建多少個新節點？
            # 迭代到下一個節點
            
            curr.next = newnode
            curr = newnode
            
            l1 = l1.next if l1 else None
            l2 =l2.next  if l2 else None

        print(res.val)
        return res.next
            
        

        
        
l1 = [2,4,3]
l2 = [5,6,4]

l1 = [0]
l2 = [0]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
obj = Solution().addTwoNumbers(l1,l2)
Solution().addTwoNumbers_v2(l1,l2)
