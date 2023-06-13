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

def DeleteNode(root,val):
    # 3 cases : Leaf Node, 1 child, 2 children
    if root is None:
        return
    if val<root.val:
        root.left=DeleteNode(root.left,val)
    elif val>root.val:
        root.left=DeleteNode(root.right,val)

    # Only 1 child exists
    if root.left is None:
        temp=root.right
        del root
        return temp
    elif root.right is None:
        temp=root.left
        del root
        return temp
    else:
        parent=root
        succ=root.right
        while succ.left is not None:
            parent=succ
            succ=succ.left
        if parent != root:
            parent.left = succ.right
        else:
            parent.right = succ.right
 
        # Copy Successor Data to root
        root.key = succ.key
 
        # Delete Successor and return root
        del succ
        return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)
    


root=BSTNode(50)
insertNode(root,30)
insertNode(root,20)
insertNode(root,40)
insertNode(root,70)
insertNode(root,60)

# inorder(root)
DeleteNode(root,60)
inorder(root)