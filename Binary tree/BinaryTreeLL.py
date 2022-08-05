class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

NewBt=TreeNode("Drinks")
leftchild=TreeNode("hot")
rightchild=TreeNode("cold")
NewBt.leftChild=leftchild
NewBt.rightChild=rightchild

def preOrderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preOrderTraversal(rootnode.leftChild)
    preOrderTraversal(rootnode.rightChild)

# preOrderTraversal(NewBt)

def inOrderTraversal(rootnode):#inward border
    if not rootnode:
        return

    inOrderTraversal(rootnode.leftChild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightChild)

# inOrderTraversal(NewBt)

def postOrderTraversal(rootnode):
    if not rootnode:
        return
    postOrderTraversal(rootnode.leftChild)
    postOrderTraversal(rootnode.rightChild)
    print(rootnode.data)
postOrderTraversal(NewBt)