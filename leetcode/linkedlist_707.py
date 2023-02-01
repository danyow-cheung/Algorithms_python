
class Node(object):
    def __init__(self,x) :
        self.val = x 
        self.next = None

class MyLinkedList_singleNode(object):

    def __init__(self):

        '''
        在链表类中实现这些功能：

        get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
        addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
        addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
        addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
        deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
        '''
        self.head = None()
        self.size = 0 # 設置一個鏈表長度的屬性，方便後續的操作，注意每次增加和刪除的時候需要進行更新

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>self.size:
            return -1 
        cur = self.head.next 
        while index:
            cur = cur.next 
            index -=1 
        return cur.val 

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 初始化這一個節點
        new_node = Node(val)
        # 新加入的節點是當前head的next節點
        new_node.next = self.head.next 
        # 當前head的節點是新加入的節點
        self.head.next = new_node
        self.size +=1# 更新長度

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        cur = self.head 
        while cur.next:
            cur = cur.next 
        cur.next = new_node
        self.size+=1 

        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<0 :
            self.addAtHead(val)
            return

        elif index==self.size:
            self.addAtTail(val)
            return
        elif index>self.self.size:
            return
        
        new_node = Node(val)
        pre = self.head 
        while index:
            pre = pre.next 
            index-=1 
        new_node.next = pre.next 
        pre.next = new_node
        self.size+=1 


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:
            return 
        pre = self.head 
        while pre.next:
            pre = pre.next 
            index-=1 
        pre.nexxt = pre.next.next 
        self.size -=1 

class Node_2(object):
    def __init__(self,val) :
        self.val = val 
        self.prev = None 
        self.next  = None

class MyLinkedList_twoNode(object):
    '''相對於單鏈表來說，添加了val的屬性'''
    def __init__(self,val):
        # 虛擬節點
        self._head = Node_2(0)
        # 虛擬節點
        self._tail = Node_2(0)
        self._head.next = self._tail
        self._tail.prev = self._head
        # 添加的節點數
        self._count = 0
    
    def _get_node(self,index):
        # 當index小與_count//2,使_head查找更快，反之_tail更快
        if index>= self._count//2:
            # 使用prev往前找
            node = self._tail
            for _ in range(self._count-index):
                node = node.prev 
        else:
            # 使用next往後找
            node = self._head 
            for _ in range(index+1):
                node = node.next 
        return node 

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if 0<= index<self._count:
            node = self._get_node(index)
            return node.val 
        else:
            return -1 

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._update(self._head,self._head.next,val)
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self._update(self._tail.prev,self._tail,val)

        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index<0:
            index = 0
        elif index>self._count:
            return
        node = self._get_node(index)
        self._update(node.prev,node,val)
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if 0<= index < self._count:
            node = self._get_node(index)
            self._count-=1 
            node.prev.next = node.next 
            node.next.prev = node.prev 
        
    def _update(self, prev,next,val):
        '''更新節點'''
        self._count+=1 
        node = Node_2(val)
        prev.next = node 
        next.prev = node 
        node.prev = prev 
        node.next = next 



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)