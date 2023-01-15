class Entry:
    def __init__(self, item, priority):
        self._item = item
        self._priority = priority
    
    def __lt__(self, other):
        return self._priority < other._priority 
    
class SortedQueue:
    def __init__(self):
        self._L = []
        
    def insert(self, item, priority):
        self._L.append(Entry(item, priority))
        self._L.sort(reverse=True)
        
    def find_min(self):
        return self._L[-1]._item
    
    def remove_min(self):
        return self._L.pop()._item
    
if __name__ == "__main__":
    s = SortedQueue()
    s.insert("burger", 3)
    s.insert("pasta", 1)
    s.insert("soda", 2)
    print(s.find_min())
    item_list = [s.remove_min() for i in range(3)]
    print(item_list)