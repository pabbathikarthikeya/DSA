class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class Binarysearchtree:
    def __init__(self):
        self.root=None
    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
        else:
            self._insert(self.root,key)
    def _insert(self,current,key):
        if key < current.key:
            if current.left is None:
                current.left=Node(key)
            else:
                self._insert(current.left,key)
        elif key > current.key:
            if current.right is None:
                current.right=Node(key)
            else:
                self._insert(current.right,key)
    def inordertraversal(self,node):
        if node is not None:
            self.inordertraversal(node.left)
            print(node.key,end=' ')
            self.inordertraversal(node.right)
    def search(self,key):
        current=self.root
        while current is not None:
            if current==None:
                return False
            if key==current.key:
                return current.key
            elif key < current.key:
                current=current.left
            else:
                current=current.right
        return False
    def findingminvalue(self):
        if self.root is None:
            return None
        current=self.root
        while current.left is not None:
            current=current.left
        return current.key
    def findingmaxvalue(self):
        if self.root is None:
            return None
        curr=self.root
        while curr.right is not None:
            curr=curr.right
        return curr.key





bst=Binarysearchtree()
bst.insert(10)
bst.insert(20)
bst.insert(3)
bst.insert(4)
bst.insert(22)
bst.insert(19)
bst.insert(12)
print("In order traversal:",end=" ")
bst.inordertraversal(bst.root)
print(bst.search(20))
print("The minimum value in the tree :",bst.findingminvalue())
print("The maximum value in the tree :",bst.findingmaxvalue())



