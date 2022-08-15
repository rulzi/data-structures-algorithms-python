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
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
    
if __name__ == '__main__':
    # numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    countries = ["USA", "UK", "China", "Indonesia"]
    
    # number_tree = build_tree(numbers)
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())
    input = input("input:")
    print(country_tree.search(input))