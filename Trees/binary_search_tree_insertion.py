class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self, val):
        self.root=self._insert(self.root, val)
    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val<node.data:
            node.left=self._insert(node.left, val)
        elif val>node.data:
            node.right=self._insert(node.right, val)
        return node
    def traverse(self):
        res=[]
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.data)
                dfs(node.right)
        dfs(self.root)
        return res
    def search(self, val):
        def searching(node, val):
            if node is None:
                return False
            if node.data==val:
                return True
            elif val>node.data:
                return searching(node.right, val)
            elif val<node.data:
                return searching(node.left, val)
        return searching(self.root, val)
bst=BST()
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)
print(bst.traverse())
print(bst.search(80))
            
    
            
    