class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
# Preorder traversal without
# recursion and without stack
def MorrisTraversalIn(root):
    curr = root
    res=[]
    while curr is not None:
        if curr.left is None:#if no left subtree
            res.append(curr.val)
            curr=curr.right
        else:
            pre=curr.left
            #finding rightmost node in left subtree
            while pre.right is not None:#at the end pre=rightmost node
                pre=pre.right 
            pre.right=curr #threaded link from rightmost child to root node to backtrack
            temp=curr
            curr=curr.left
            temp.left=None
    return res
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
 
root.left.left = Node(4)
root.left.right = Node(5)
 
root.right.left= Node(6)
root.right.right = Node(7)
 
root.left.left.left = Node(8)
root.left.left.right = Node(9)
 
root.left.right.left = Node(10)
root.left.right.right = Node(11)
 
print(MorrisTraversalIn(root))
            
            
            
