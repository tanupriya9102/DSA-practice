class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

def PreMorris(root):
    res=[]
    curr=root
    while curr is not None:
        res.append(curr.val)
        if curr.left is None:
            curr=curr.right
        else:
            pre=curr.left
            while(pre.right is not None):
                pre=pre.right
            pre.right=curr.right #threaded link from rightmost child to root.right node to backtrack
            temp=curr
            curr=curr.left
            temp.right=None #destroy the link bw root and root.right
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
 
print(PreMorris(root))
            
    
        
        
        
