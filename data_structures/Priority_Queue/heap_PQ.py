# This is an efficient version of priority queue where we use heap data structure

from heap import Heap, Entry

class HeapPQ(Heap):
    def __init__(self,
                items=(),               # list of just items
                entries = (),           # list of (item, priority) pairs
                key = lambda x: x):     # by modifying the lambda function to lambda x: -x, we can implement max heap
        self._key = key
        self._entries = [Entry(item, priority) for item, priority in entries]
        self._entries.extend([Entry(item, key(item)) for item in items])
        self._itemMap = {entry._item: index for index, entry in enumerate(self._entries)}
        self._heapify()
        
    def _swap(self, a, b):
        L = self._entries
        Va = L[a]._item
        Vb = L[b]._item
        self._itemMap[Va] = b
        self._itemMap[Vb] = a
        L[a], L[b] = L[b], L[a]
        
    def insert(self, item, priority = None):
        if priority == None:
            priority = self._key(item)
        L = self._entries
        index = len(L)
        L.append(Entry(item, priority))
        self._itemMap[item] = index
        self._upHeap(index)
        
    def change_priority(self, item, priority = None):
        if priority == None:
            priority = self._key(item)
        index = self._itemMap[item]
        self._entries[index]._priority = priority
        self._upHeap(index)
        self._downHeap(index)
        
    def remove_min(self):
        L = self._entries
        item = L[0]._item
        self._swap(0, len(L)-1)
        del self._itemMap[item]
        L.pop()
        self._downHeap(0)
        return item 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self) > 0:
            return self.remove_min()
        else:
            raise StopIteration
        
def heap_sort(l):
    H = HeapPQ(items=l)
    l[:] = [item for item in H]
        

if __name__ == "__main__":
    L = [34, 9, 12, 1, 32, 56, 2]
    heap_sort(L)
    print(L)

    max_heap = HeapPQ(key=lambda x: -x)
    for i in range(10):
        max_heap.insert(i)

    l = [max_heap.remove_min() for i in range(10)]
    print(l)