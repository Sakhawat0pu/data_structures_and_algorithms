from adjacencySet import AdjacencySet

class Graph(AdjacencySet):
    def __init__(self, V, E):
        super().__init__(V, E)
        
    def dfs1(self, v):
        visited = {v}
        self._dfs1(v, visited)
        return visited
    
    def _dfs1(self, v, visited):
        for n in self.neighbors(v):
            if n not in visited:
                visited.add(n)
                self._dfs1(n, visited)
                
    def dfs2(self, v):
        visited = {v: None}
        self._dfs2(v, visited)
        return visited
    
    def _dfs2(self, v, visited):
        for n in self.neighbors(v):
            if n not in visited:
                visited[n] = v
                self._dfs2(n, visited)
                
    def dfs3(self, v):
        tree = {}
        stack = [(None, v)]
        
        while stack:
            a, b = stack.pop()
            if b not in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    stack.append((b, n))
        return tree
    
if __name__ == "__main__":
    vs = {1, 3, 2, 4, 5, 6}
    es = {
        (1, 2), (1, 3), (1, 4),
        (2, 1), (2, 3),
        (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),
        (4, 1), (4, 3), (4, 6),
        (5, 3), (5, 6),
        (6, 3), (6, 4), (6, 5)
        }
    g = Graph(vs, es)
    print(g.dfs1(4))
    print(g.dfs2(4))
    print(g.dfs3(4))