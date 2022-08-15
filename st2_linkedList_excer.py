'''
Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction. Your node class will look this this,
'''
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def atBegining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
        
    def atEnd(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None, itr)
        
    def insertVal(self, data_list):
        self.head = None
        for data in data_list:
            self.atEnd(data)       
        
    def print(self):
        if self.head is None:
            print("LinkList is empty")
            return
        
        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data)+ '-->'
            itr = itr.next
        
        print(llstr)
        
    def printprev(self):
        if self.head is None:
            print("LinkList is empty")
            return
        
        itr = self.head        
        while itr.next:
            itr = itr.next
            
        itrprev = itr
        llstr = ""
        while itrprev:
            llstr += str(itrprev.data)+ '<--'
            itrprev = itrprev.prev
        
        print(llstr)
                
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
    def removeAt(self, index):
        if (index < 0) or (index >= self.getLength()):
            raise Exception("not valid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if index-1 == count:
                itr.next.next.prev = itr
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def rearangeprev(self):
        itr = self.head  
        prev = None
        while itr.next:
            itr.prev = prev
            prev = itr
            itr = itr.next
            
    def insertAt(self, index, data):
        if (index < 0) or (index >= self.getLength()):
            raise Exception("not valid index")
        
        if index == 0:
            self.atBegining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if index-1 == count:
                node = Node(data, itr.next, itr)
                itr.next = node
                break
            itr = itr.next
            count += 1
        
        self.rearangeprev()
    
    def insertAfterValue(self, dataAfter, data):
        itr = self.head
        while itr:
            if itr.next is not None:
                if dataAfter == itr.data:
                    itr.next = Node(data, itr.next, itr)
            itr = itr.next
            
        self.rearangeprev()
    
    def removeValue(self, data):
        if self.head.data == data:
            self.head = self.head.next
            
        itr = self.head
        
        while itr:
            if itr.next is not None:
                if data == itr.next.data:
                    itr.next = itr.next.next
            itr = itr.next
            
        self.rearangeprev()
        
        
ll = LinkedList()
ll.print()