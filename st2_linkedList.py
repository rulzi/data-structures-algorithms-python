class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def atBegining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def atEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
        
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
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
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
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1
    
    def insertAfterValue(self, dataAfter, data):
        itr = self.head
        while itr:
            if itr.next is not None:
                if dataAfter == itr.data:
                    itr.next = Node(data, itr.next)
            itr = itr.next
    
    def removeValue(self, data):
        if self.head.data == data:
            self.head = self.head.next
            
        itr = self.head
        
        while itr:
            if itr.next is not None:
                if data == itr.next.data:
                    itr.next = itr.next.next
                
            itr = itr.next
        
        
ll = LinkedList()
ll.print()