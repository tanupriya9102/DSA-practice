class Queue:
    def __init__(self):
        self.list=[]

    def __str__(self): #shows how stack looks else would return address
        values=[str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    
    def enqueue(self,n):
        self.list.append(n)
        return "Sucessfully inserted!"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty.Nothing to remove!!"
        
        else:
            self.list.pop(0)
            return "deleted"


    def peek(self):
        if(self.isEmpty()):
            return "list is empty"
        else:
            return self.list[0]

    def delete(self):
        self.list=None
        return self.list

        


q=Queue()
# print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
# print(q.peek())
# q.dequeue()
# print(q.isEmpty())
print(q)
# print(q.peek())
# print(q.delete())
