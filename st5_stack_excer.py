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
    
    

'''
Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial
'''

def reverse_string(val):
    stack = Stack()
    
    string = ""
    for i in val:
        stack.push(i)
        
    for i in range(stack.size()):
        string += stack.pop()
        
    return string

'''
Write a function in python that checks if paranthesis in the string are balanced or not.
Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
'''
def is_balanced(val):
    stack = Stack()
    
    parantheses_pair = {
        "{" : "}",
        "[" : "]",
        "(" : ")",
    }
    
    balance = False
    
    for i in val:
        if i in parantheses_pair.keys():
            stack.push(i)
            balance = True
            
        if not stack.is_empty():
            if i in parantheses_pair.values():
                if parantheses_pair[stack.peek()] != i:
                    return False
                stack.pop()
            
    return balance
     

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
print(is_balanced("(a*b+}c+1{)"))