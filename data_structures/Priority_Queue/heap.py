class Entry:
    def __init__(self, item, priority):
        self._item = item
        self._priority = priority
    
    def __lt__(self, other):
        return self._priority < other._priority 

class Heap:
    def __init__(self):
        self._entries = []
        
    def __len__(self):
        return len(self._entries)
    
    def parent(self, ind):
        return (ind - 1) // 2
    
    def children(self, ind):
        left = ind * 2 + 1
        right = ind * 2 + 2
        return range(left, min(len(self._entries), right + 1))
    
    def _swap(self, a, b):
        L = self._entries
        L[a], L[b] = L[b], L[a]
    
    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._upHeap(len(self._entries) - 1)
    
    def _upHeap(self, ind):
        L = self._entries
        parent = self.parent(ind)
        if ind > 0 and L[parent] > L[ind]:
            self._swap(ind, parent)
            self._upHeap(parent)
    
    def find_min(self):
        return self._entries[0]._item
    
    def remove_min(self):
        L = self._entries
        item = L[0]._item
        L[0] = L[-1]
        L.pop()
        self._downHeap(0)
        return item
    
    def _downHeap(self, ind):
        L = self._entries
        children = self.children(ind)
        if children:
            child = min(children, key = lambda x: L[x])
            if L[child] < L[ind]:
                self._swap(ind, child)
                self._downHeap(child)
                
    def _heapify(self):
        n = len(self)
        for i in reversed(range(n)):
            self._downHeap(i)
            

    
    
if __name__ == "__main__":
    s = Heap()
    s.insert("burger", 3)
    s.insert("pasta", 1)
    s.insert("soda", 2)
    print(s.find_min())
    item_list = [s.remove_min() for i in range(3)]
    print(item_list)