class EdgeSet:
    def __init__(self, V = (), E = ()):
        self._vertex = set()
        self._edge = set()
        for v in V: self.add_vertex(v)
        for v, u in E: self.add_edge(v, u)
        
    def vertex(self):
        return self._vertex 
    
    def edge(self):
        return self._edge 

    def add_vertex(self, v):
        self._vertex.add(v)
    
    def add_edge(self, v, u):
        self._edge.add((v, u))
        
    def remove_vertex(self, v):
        self._vertex.remove(v)
    
    def remove_edge(self, v, u):
        self._edge.remove((v, u))
    
    def neighbors(self, v):
        return [w for u, w in self._edge if u == v]
    
    def __iter__(self):
        return iter(self._vertex)

class Graph(EdgeSet):
    def __init__(self, V, E):
        super().__init__(V, E)
        
if __name__ == "__main__":
    V = {1, 2, 3, 4}
    E = {(1, 2), (1, 4), (2, 3), (3, 4), (4, 2)}
    G = Graph(V, E)
    print(G.neighbors(1))
    print(G.edge())