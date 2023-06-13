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


def search(root,val):
    if root is None:
        return "Value not present!!"
    elif root.val==val:
        return "Value found!"
    elif(val<root.val):
        return search(root.left,val)
    elif(val>root.val):
        return search(root.right,val)
    
   

root=BSTNode(None)
insertNode(root,2)
insertNode(root,12)
insertNode(root,1)
insertNode(root,4)
insertNode(root,11)

# print(newBST.right.val)
# print(newBST.left.left.val)
print(search(root,12))