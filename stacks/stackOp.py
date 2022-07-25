
from sqlalchemy import true


class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=reversed(self.list)
        values=[str(x) for x in values]
        return '\n'.join(values)

    def push(self,n):
        self.list.append(n)
        return "Sucessfully inserted!"

    # def pop(self):
    #     return(self.stk.pop())

    # def peek(self):
    #     return(self.stk[-1])

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    # def isfull(self)

    # def delete(self):
    #     return del stack

s=Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)
print(s.isEmpty())