# queue with capacity

class Queue:
    def __init__(self,limit):
        self.items=limit*[None]
        self.limit=limit
        self.start=-1
        self.top=-1

    def __str__(self): 
        values=[str(x) for x in self.list]
        return ' '.join(values)

    def isFull(self):
        if (self.top+1==self.start or (self.start==0 and self.top+1==self.limit)):
            return True
        else:
            return False

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

    def enqueue(self,n)




q=Queue(2)
print(q.isFull())
    

   