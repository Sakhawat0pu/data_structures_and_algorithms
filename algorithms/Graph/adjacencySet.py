class AdjacencySet:
    def __init__(self, V = (), E = ()):
        self._vertex = set()
        self._neighbors = {}
        for v in V: self.add_vertex(v)
        for v, u in E: self.add_edge(v, u)
    
    def vertex(self):
        return self._vertex
    
    def edge(self):
        for v in self._neighbors:
            for u in self._neighbors[v]:
                yield (v, u)
    
    def add_vertex(self, v):
        if v not in self._neighbors and v not in self._vertex:
            self._vertex.add(v)
            self._neighbors[v] = []
            
    def add_edge(self, v, u):
        if v in self._neighbors and u in self._neighbors:
            self._neighbors[v].append(u)
            # self._neighbors[u].append(v)
            
    def remove_vertex(self, v):
        if v in self._neighbors and v in self._vertex:
            self._vertex.remove(v)
            for u in self._neighbors[v]:
                self._neighbors[u].remove(v)
            del self._neighbors[v]
            
    def remove_edge(self, v, u):
        if v in self._neighbors and u in self._neighbors:
            try:
                self._neighbors[v].remove(u)
                self._neighbors[u].remove(v)
            except ValueError:
                pass
            
    def neighbors(self, v):
        return self._neighbors[v]
    
    def print_adjList(self):
        for v in self._neighbors:
            print(f"{v} : {self._neighbors[v]}")
    
    def __iter__(self):
        return iter(self._vertex)
    
class Graph(AdjacencySet):
    def __init__(self, V, E):
        super().__init__(V, E)
        
if __name__ == "__main__":
    vs = {1, 3, 2, 4, 5, 6}
    es = {(1, 2), (1, 3), (1, 4),
        (2, 1), (2, 3),
        (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),
        (4, 1), (4, 3), (4, 6),
        (5, 3), (5, 6),
        (6, 3), (6, 4), (6, 5)}
    g = Graph(vs, es)

    print(g.neighbors(1))
    edge = set()
    for i in g.edge():
        edge.add(i)
    print(edge)
    g.remove_edge(3, 6)
    g.print_adjList()
    print()
    g.remove_vertex(6)
    g.print_adjList() 
    



