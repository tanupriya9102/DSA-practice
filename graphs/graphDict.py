
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

d={'a':['b','c'],
   'b':['d','e'],
   'c':['a','e'],
   'd':['b','e','f'],
   'e':['b','d','f'],
   }

graph=Graph(d)
print(graph.gdict)
graph.addVertex('f')
print(graph.gdict)
graph.addEdge('f','d')
print(graph.gdict)
graph.addEdge('f','e')
print(graph.gdict)

