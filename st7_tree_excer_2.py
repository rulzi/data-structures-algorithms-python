class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level
        
    def print_tree(self, level):
        spaces = ' '*self.get_level()*3
        prefix = spaces+'|__' if self.parent else ""
        print(prefix + self.data)
        level -= 1
        if self.children and level+1:
            for child in self.children:
                child.print_tree(level)
        
def build_product_tree():
    root = TreeNode("Global") 
    indonesia = TreeNode("indonesia")
    jabar = TreeNode("Jawa Barat")
    jatim = TreeNode("Jawa Timur")
    
    jabar.add_child(TreeNode("Bogor"))
    jabar.add_child(TreeNode("Tasikmalaya"))
    jabar.add_child(TreeNode("Bandung"))
    jatim.add_child(TreeNode("Surabaya"))
    jatim.add_child(TreeNode("Malang"))
    jatim.add_child(TreeNode("Nganjuk"))
    
    indonesia.add_child(jabar)
    indonesia.add_child(jatim)
    
    usa = TreeNode("USA")
    nj = TreeNode("New Jersey")
    cl = TreeNode("California")
    
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))
    cl.add_child(TreeNode("San Fransisco"))
    cl.add_child(TreeNode("Mountain View"))
    cl.add_child(TreeNode("Palo Alto"))
    
    usa.add_child(nj)
    usa.add_child(cl)
    
    root.add_child(indonesia)
    root.add_child(usa)
    
    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree(3)
    pass