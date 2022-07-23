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

    # insert in liked list
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


Sll = SLinkedList()
Sll.insert(1, 1)
Sll.insert(2, -1)
Sll.insert(3, -1)
Sll.insert(4, -1)
Sll.insert(0, 0)
Sll.insert(0, 3)
Sll.insert(11, 1)

print([node.value for node in Sll])
