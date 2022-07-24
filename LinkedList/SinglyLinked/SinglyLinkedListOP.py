class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # for printing linked list

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert nodes in linked list after a give index
    def insert(self, value, location):
        newNode = Node(value)
        # if List doesnt have an element yet
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # element to be added on 0th index (beginning)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # element to be added at the end
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            # element to be added at particular index
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    # traversal of singly linked list
    def traverse(self):
        if self.head is None:
            print("Linked list doesn't exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # searching linked list
    def searching(self, svalue):
         if self.head is None:
            return (print("Linked list doesn't exist"))
         else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == svalue:
                   # gives 1st index where element found to consider all index change return to print
                   return(print("Index at which element is present=", index))
                node = node.next
                index += 1

            return(print("value doesn't exist in list!!"))
    # deleting elements from linked list 
    def delete(self, location):
        if self.head is None:
            return (print("Linked list doesn't exist"))
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next #node's adderess stored in head's next

            elif location==-1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next










        




Sll = SLinkedList()
Sll.insert(1, 3)
Sll.insert(2,-1)
Sll.insert(3,-1)
Sll.insert(4,-1)
Sll.insert(5,3)
Sll.insert(6,2) #order of list will change=>position of 5 will not be 3 but will become 4
Sll.insert(7,1)
Sll.insert(7,-1)
print([node.value for node in Sll])
# Sll.traverse()
# Sll.searching(7)
# Sll.searching(8)
Sll.delete(-1)
print([node.value for node in Sll])

Sll1 = SLinkedList()
Sll1.insert(1,0)
print([node.value for node in Sll1])
Sll1.delete(0)
print([node.value for node in Sll1])