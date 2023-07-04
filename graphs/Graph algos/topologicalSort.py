from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.vertices = v

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortutil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortutil(i, visited, stack)

        stack.insert(0,v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortutil(k, visited, stack)

        print(stack)

graph = Graph(8)
graph.addEdge('a', 'c')
graph.addEdge('c', 'e')
graph.addEdge('e', 'h')
graph.addEdge('e', 'f')
graph.addEdge('f', 'g')
graph.addEdge('b', 'd')
graph.addEdge('b', 'c')
graph.addEdge('d', 'f')
graph.topologicalSort()
