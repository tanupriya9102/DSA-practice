#Deepest node using level order traversal BFS using queues

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def deepestNode(root):
    if not root:
        return "Invalid root"
    queue=[]
    queue.append(root)
    while len(queue)>0:
        node=queue.pop(0)
        
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    deepestVal=node.val
    return deepestVal
        

        
        
        
root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(8)
print(deepestNode(root))
