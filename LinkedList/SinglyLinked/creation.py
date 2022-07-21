class Node:
    def __init__(self,value=None):
        self.value= value
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

Sll=SLinkedList()
node1=Node(1)
node2=Node(2)

Sll.head=node1
Sll.head.next=node2
Sll.tail=node2