class BSTNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def insertNode(root,val): #O(log n)
    if root.val is None:
        root.val=val
    elif(val<=root.val):
        if root.left is None:
            root.left=BSTNode(val)
        else:
            insertNode(root.left,val)

    else:
        if root.right is None:
            root.right=BSTNode(val)
        else:
            insertNode(root.right,val)

    return "Node inserted successfully"

def preOrder(root):
    if root is None:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)




root=BSTNode(10)
insertNode(root,2)
insertNode(root,12)
insertNode(root,1)
insertNode(root,4)
insertNode(root,11)
# insertNode(root,10)
insertNode(root,14)
# print(root.val)
inOrder(root)
