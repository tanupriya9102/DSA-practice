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


newBST=BSTNode(None)
print(insertNode(newBST,70))
print(insertNode(newBST,60))
print(insertNode(newBST,50))
print(insertNode(newBST,80))

print(newBST.right.val)
print(newBST.left.left.val)