
class Stack:
    def __init__(self,limit):
        self.limit=limit
        self.list=[]

    def __str__(self): #shows how stack looks else would return address
        values=reversed(self.list)
        values=[str(x) for x in values]
        return '\n'.join(values)

    def isFull(self):
        if len(self.list)==self.limit:
            return True

        else:
            return False


    def push(self,n):
        if self.isFull():
            return "Stack is full"
        else:
            self.list.append(n)
            return "Sucessfully inserted!"

        

    def pop(self):
        if(self.isEmpty()):
            return "list is empty"
        else:
            return self.list.pop()
  
        

    def peek(self): #returns top most element in stack (last element(LIFO))
        if(self.isEmpty()):
            return "list is empty"
        else:
            return self.list[-1]
        

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def delete(self):
        self.list=None
        return self.list

    # def isfull(self)

    # def delete(self):
    #     return del stack

s=Stack(3)

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
# print(s)
# print(s.isEmpty())
# print(s.peek())
# print(s.delete())