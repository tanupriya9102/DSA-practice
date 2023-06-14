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


def heapifyInsert(root,index,heapType):
    parent=int(index/2)
    if index<=1:
        return
    if heapType=='min':
        if root.customList[index]<root.customList[parent]:
            temp=root.customList[index]
            root.customList[index]=root.customList[parent]
            root.customList[parent]=temp
        heapifyInsert(root,parent,heapType)
    elif heapType=='max':
        if root.customList[index]>root.customList[parent]:
            temp=root.customList[index]
            root.customList[index]=root.customList[parent]
            root.customList[parent]=temp
        heapifyInsert(root,parent,heapType)

def Insert(root,value,heapType):
    if root.heapSize +1==root.maxSize:
        return "The heap is full!!"
    root.customList[root.heapSize +1]=value
    root.heapSize+=1
    heapifyInsert(root,root.heapSize,heapType)
    return "Value Inserted!"
Bheap=Heap(10)
# print(sizeHeap(Bheap))
Insert(Bheap,4,'max')
Insert(Bheap,5,'max')
Insert(Bheap,2,'max')
Insert(Bheap,1,'max')
Insert(Bheap,6,'max')
# Insert(Bheap,8,'max')
Insert(Bheap,0,'max')
levelOrder(Bheap)