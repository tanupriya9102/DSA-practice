#searching node in a Binary tree using Level Order Traversal
class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def Search(root,val):
    if not root:
        return "Invalid root"
    res=[]
    next_queue=[]
    queue=[]
    queue.append(root)
    while len(queue)>0:
        node=queue.pop(0)
        if node.val==val:
            return(True)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return False
            
 
    
    
root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
# root.right.right.left=Node(8)

print(Search(root,2))
    
