#level order traversal BFS using queues

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def LevelOrder(root):
    if root is None:
        return 
    queue=[]
    queue.append(root)
    
    while len(queue)>0:
        print(queue[0].val,end=" ")
        node=queue.pop(0)
        # queue.pop(0)
        
        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)
        
        
        
root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print("Level Order Traversal of binary tree is -")
LevelOrder(root)
