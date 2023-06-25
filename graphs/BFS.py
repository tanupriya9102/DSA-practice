class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def addEdge(self,vertex,edge):
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
    
    def bfs(self,vertex=None):
        if not vertex:
            vertex=list(self.gdict.keys())[0]
        visited=set()
        visited.add(vertex)
        queue=[vertex]
        while queue:
            current_vertex=queue.pop(0)
            print(current_vertex)
            for adjacent_vertex in self.gdict[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)










d={'a':['b','c'],
   'b':['a','e'],
   'c':['a','d'],
   'd':['c','e'],
   'e':['b','d']
   }

graph=Graph(d)
graph.bfs()