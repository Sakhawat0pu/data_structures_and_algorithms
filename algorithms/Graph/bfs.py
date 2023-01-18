# we can use same algorithm for bfs and dfs. The only difference is in bfs we maintain a queue and dfs we maintain a stack
# In bfs, we maintain first in, first out order and in dfs, we maintain list in, first out order

from adjacencySet import AdjacencySet

class Graph(AdjacencySet):
    def __init__(self, V, E):
        super().__init__(V, E)
        
    def bfs(self, v):
        tree = {}
        queue = [(None, v)]
        
        while queue:
            a, b = queue.pop(0)         # popping the first item and we will be appending to the end
            if b not in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    queue.append((b, n))
        
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
    print(g.bfs(4))