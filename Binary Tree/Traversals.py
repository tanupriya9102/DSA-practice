#using recursion
class Node:
    def __init__(self,val):
        self.val=val
        self.left= None
        self.right= None
        
        
def PreOrder(root):
    if root:
        print(root.val)
        PreOrder(root.left)
        PreOrder(root.right)
        
def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.val)
        InOrder(root.right)

def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.val)
        
        
        
root=Node(1)
root.left=Node(2)
root.right=Node(5)

root.left.left=Node(3)
root.left.right=Node(4)

root.right.left=Node(6)
root.right.right=Node(7)
print("Preorder traversal:")
PreOrder(root)
print("Inorder traversal:")
InOrder(root)
print("Postorder traversal:")
PostOrder(root)
