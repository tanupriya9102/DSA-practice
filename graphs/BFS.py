from collections import deque
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    
    def bfs(self,vertex=None):
        if not vertex:
            vertex=list(self.gdict.keys())[0]
        visited=set()
        visited.add(vertex)
        # queue=[vertex]
        queue=deque([vertex]) #to reduce time complexity

        while queue:
            # current_vertex=queue.pop(0) =>O(n)
            current_vertex=queue.popleft() #O(1)

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