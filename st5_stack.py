from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

# stack.append("https://www.cnn.com/")
# stack.append("https://www.cnn.com/world")
# stack.append("https://www.cnn.com/china")
# stack.append("https://www.cnn.com/indonesia")

stack = Stack()