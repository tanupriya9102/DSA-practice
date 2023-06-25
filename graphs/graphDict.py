

class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        # if(self.gdict[vertex]is None):
        #     self.gdict[vertex]=edge  
        # else:
        self.gdict[vertex].append(edge)

    def addVertex(self,vertex):
        self.gdict[vertex]=[]

    def delEdge(self,vertex,edge):
        self.gdict[vertex].remove(edge)
    def delVertex(self,vertex):
        del self.gdict[vertex]
        for i in self.gdict:
            if vertex in self.gdict[i]:
                self.gdict[i].remove(vertex)

  

d={'a':['b','c'],
   'b':['d','e'],
   'c':['a','e'],
   'd':['b','e','f'],
   'e':['b','d','f'],
   'f':['']
   }

graph=Graph(d)
# print(graph.gdict)
graph.addVertex('f')
# print(graph.gdict)
graph.addEdge('f','d')
# print(graph.gdict)
graph.addEdge('f','e')
print(graph.gdict)
print('---------------------------------------------------------------------------------------------')
# graph.delEdge('f','e')
# print(graph.gdict)
graph.delVertex('f')
print(graph.gdict)