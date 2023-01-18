class Entry:
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        return self.priority < other.priority


class HeapPQ:
    def __init__(self):
        self._entries = []

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._upheap(len(self._entries)-1)

    def parent(self, i):
        return (i-1)//2

    def children(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        return range(left, min(len(self._entries), right + 1))

    def _swap(self, a, b):
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        L = self._entries
        parent = self.parent(i)
        if i > 0 and L[i] < L[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def find_min(self):
        return self._entries[0].item

    def remove_min(self):
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        return item

    def _downheap(self, i):
        L = self._entries
        children = self.children(i)
        if children:
            child = min(children, key=lambda x: L[x])
            if L[child] < L[i]:
                self._swap(i, child)
                self._downheap(child)

    def __len__(self):
        return len(self._entries)

    def _heapify(self):
        n = len(self._entries)
        for i in reversed(range(n)):
            self._downheap(i)


class PriorityQueue(HeapPQ):
    def __init__(self,
                items=(),
                entries=(),
                key=lambda x: x):
        self.key = key
        self._entries = [Entry(i, p) for i, p in entries]
        self._entries.extend([Entry(i, key(i)) for i in items])
        self._itemMap = {entry.item: index for index, entry in enumerate(self._entries)}
        self._heapify()

    def insert(self, item, priority=None):
        if priority is None:
            priority = self.key(item)
        index = len(self._entries)
        self._entries.append(Entry(item, priority))
        self._itemMap[item] = index
        self._upheap(index)

    def swap(self, a, b):
        L = self._entries
        Va = L[a].item
        Vb = L[b].item
        self._itemMap[Va] = b
        self._itemMap[Vb] = a
        L[a], L[b] = L[b], L[a]

    def change_priority(self, item, priority=None):
        if priority is None:
            priority = self.key(item)
        index = self._itemMap[item]
        self._entries[index].priority = priority
        self._upheap(index)
        self._downheap(index)

    def remove_min(self):
        L = self._entries
        item = L[0].item
        self.swap(0, len(L)-1)
        del self._itemMap[item]
        L.pop()
        self._downheap(0)
        return item

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) > 0:
            return self.remove_min()
        else:
            raise StopIteration
        
class AdjacencySet:
    def __init__(self, V, E):
        self._vertex = set()
        self._neighbors = {}
        for v in V: self.add_vertex(v)
        for e in E:
            if len(e) == 3:
                u, v, w = e 
                self.add_edge(u,v,w)
            else:
                u, v = e
                self.add_edge(u,v)
                
    def add_vertex(self, v):
        if v not in self._vertex and v not in self._neighbors:
            self._vertex.add(v)
            self._neighbors[v] = {}
    
    def add_edge(self, u, v, w=1):
        if u in self._neighbors and v in self._neighbors:
            self._neighbors[u][v] = w
            
    def neighbors(self, v):
        return [u for u in self._neighbors[v]]
    
    def remove_vertex(self, v):
        if v in self._neighbors and v in self._vertex:
            self._vertex.remove(v)
            for u in self.neighbors(v):
                del self._neighbors[u][v]
            del self._neighbors[v]
            
    def remove_edge(self, u, v):
        if u in self._neighbors and v in self._neighbors:
            try:
                del self._neighbors[u][v]
                del self._neighbors[v][u]
            except ValueError:
                pass
    def weight(self, u, v):
        return self._neighbors[u][v]
    
    
class Graph(AdjacencySet):
    def __init__(self, V, E):
        super().__init__(V, E)
    
    def dijkstra(self, v):
        tree = {}
        D = {v: 0}
        to_visit = PriorityQueue()
        to_visit.insert((None, v), 0)
        for a, b in to_visit:
            if b not in tree:
                tree[b] = a
                if a is not None:
                    D[b] = D[a] + self.weight(a, b)
                for n in self.neighbors(b):
                    if (a, b) == (n, b):
                        to_visit.insert((b, n), self.weight(b, n))
                    else:
                        to_visit.insert((b, n), D[b] + self.weight(b, n))
        return tree, D
    
    def primm(self, v):
        tree = {}
        to_visit = PriorityQueue()
        to_visit.insert((None, v), 0)
        for a, b in to_visit:
            if b not in tree:
                tree[b] = a
                for n in self.neighbors(b):
                    to_visit.insert((b, n), self.weight(b, n))
        return tree            
            
                    
if __name__ == "__main__":
    vs = {1, 3, 2, 4, 5, 6}
    es = {
        (1, 2, 2), (1, 3, 4), (1, 4, 1),
        (2, 1, 2), (2, 3, 1),
        (3, 1, 4), (3, 2, 1), (3, 4, 5), (3, 5, 1), (3, 6, 3),
        (4, 1, 1), (4, 3, 5), (4, 6, 3),
        (5, 3, 1), (5, 6, 1),
        (6, 3, 3), (6, 4, 3), (6, 5, 1)
        }
    g = Graph(vs, es)
    tree, D = g.dijkstra(2)
    print(tree)
    print(D)
    print(g.primm(2))