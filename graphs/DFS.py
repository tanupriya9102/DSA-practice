class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def dfs(self,vertex=None):
        if not vertex:
            vertex=list(self.gdict.keys())[0]
        visited=set()
        stack=[vertex]
        while stack:
            current_vertex=stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                
            for adjacent_vertex in self.gdict[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)


d={'a':['b','c'],
   'b':['a','e'],
   'c':['a','d'],
   'd':['c','e'],
   'e':['b','d']
   }

graph=Graph(d)
graph.dfs('a')