class Heap:
    def __init__(self,size):
        self.customList=(size+1)* [None]
        self.heapSize=0
        self.maxSize=size+1

def peek(root):
    if not root:
        return 
    else:
        return root.customList[1]
    
def sizeHeap(root):
    if not root:
        return 
    else:
        return root.heapSize

def levelOrder(root):
    if not root:
        return 
    else:
        for i in range(1,root.heapSize+1):
            print(root.customList[i])



Bheap=Heap(5)
print(sizeHeap(Bheap))