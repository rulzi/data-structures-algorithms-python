class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
        
    def print_tree(self, type):
        spaces = ' '*self.get_level()*3
        prefix = spaces+'|__' if self.parent else ""
        if type == "name":
            print(prefix + self.name)
        if type == "designation":
            print(prefix + self.designation)
        if type == "both":
            print(prefix + self.name + " ("+self.designation+")")
        if self.children:
            for child in self.children:
                child.print_tree(type)
        
def build_product_tree():
    ceo = TreeNode("Nilupul", "CEO") 
    cto = TreeNode("Chinmay", "CTO")
    ih = TreeNode("Visha", "Infrastructur Head")
    ah = TreeNode("Aamir", "Application Head")
    cm = TreeNode("Dhaval", "Cloud Manager")
    am = TreeNode("Abhijit", "App Manager")
    hr = TreeNode("Gels", "HR Head")
    rm = TreeNode("Peter", "Recruiter Manager")
    pm = TreeNode("Waqas", "Police Manager")
    
    ih.add_child(cm)
    ih.add_child(am)
    
    cto.add_child(ih)
    cto.add_child(ah)
    
    hr.add_child(rm)
    hr.add_child(pm)
    
    ceo.add_child(cto)
    ceo.add_child(hr)
    
    return ceo

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree("name")
    root.print_tree("designation")
    root.print_tree("both")
    pass