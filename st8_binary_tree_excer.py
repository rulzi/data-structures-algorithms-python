from unittest import result


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    def in_order_traversal(self):
        elements = []
        
        # Left Tree
        if self.left:
            elements += self.left.in_order_traversal()
            
        # Base Node
        elements.append(self.data)
        
        # Right Tree
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            
        return False
    
    # find_min(): finds minimum element in entire binary tree
    def find_min(self):
        if self.left:
            return self.left.find_min()
        
        return self.data
    
    # find_max(): finds maximum element in entire binary tree
    def find_max(self):
        if self.right:
            return self.right.find_max()
        
        return self.data
    
    # calculate_sum(): calcualtes sum of all elements
    def calculate_sum(self):
        sum_value = 0
        
        if self.left:
            sum_value += self.left.calculate_sum()
            
        if self.right:
            sum_value += self.right.calculate_sum()
            
        sum_value += self.data
        
        return sum_value
    
    # post_order_traversal(): performs post order traversal of a binary tree
    def post_order_traversal(self):
        elements = []
        
        # Left Tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        # Right Tree
        if self.right:
            elements += self.right.in_order_traversal()
            
        # Base Node
        elements.append(self.data)
            
        return elements
    
    # pre_order_traversal(): perofrms pre order traversal of a binary tree
    def pre_order_traversal(self):
        elements = []
        
        # Base Node
        elements.append(self.data)
        
        # Left Tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        # Right Tree
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
    
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    
    number_tree = build_tree(numbers)
    print(number_tree.pre_order_traversal())