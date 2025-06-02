class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=TreeNode(value)
        else:
            curr=self.root
            while True:
                if value < curr.value:
                    if curr.left is None:
                        curr.left=TreeNode(value)
                        break
                    curr=curr.left
                elif value > curr.value:
                    if curr.right is None:
                        curr.right=TreeNode(value)
                        break
                    curr=curr.right
                else:
                    break
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value,end=" ")
            self.inorder(root.right)

elements=[50, 30, 70, 20, 40, 60, 80]
bst=BST()
for val in elements:
    bst.insert(val)

print("Inorder traversal")
bst.inorder(bst.root)


        



