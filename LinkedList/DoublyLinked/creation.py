class Node:
    def __init__(self,value=None):
        self.value= value
        self.next=None
        self.prev=None

class DLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
# for printing linked list
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    
    def createDll(self,nodeVal):
        node=Node(nodeVal)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
        return("Dll created!!")


Dll=DLinkedList()
Dll.createDll(5)
print([node.value for node in Dll])



    



