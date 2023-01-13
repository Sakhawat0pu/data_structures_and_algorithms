class Entry:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        
class Mapping:
    def __init__(self):
        self._nBuckets = 2
        self._L = [[] for i in range(self._nBuckets)]
        self._len = 0
        
    def _hash(self, key):
        return hash(key) % self._nBuckets
    
    def _rehash(self):
        self._nBuckets *= 2
        new_L = [[] for i in range(self._nBuckets)]
        for bucket in self._L:
            for obj in bucket:
                bucket_ind = self._hash(obj._key)
                new_L[bucket_ind].append(obj)
        self._L = new_L
        
    def __setitem__(self, key, value):
        bucket_ind = self._hash(key)
        for obj in self._L[bucket_ind]:
            if obj._key == key:
                obj._value = value
                return
        self._L[bucket_ind].append(Entry(key, value))
        self._len += 1
        
        if self._len > self._nBuckets:
            self._rehash()
            
    def __getitem__(self, key):
        bucket_ind = self._hash(key)
        for obj in self._L[bucket_ind]:
            if obj._key == key:
                return obj._value  
        raise KeyError(f"Key {key} does not exist in the dictionary!!")
    
    def remove(self, key):
        bucket_ind = self._hash(key)
        for obj in self._L[bucket_ind]:
            if obj._key == key:
                self._L[bucket_ind].remove(obj)
                self._len -= 1
                return
        raise KeyError(f"Key {key} does not exist in the dictionary!!")
        
    def __len__(self):
        return self._len

if __name__ == "__main__":
    hash_table = Mapping()
    for i in range(10):
        hash_table[i] = str(i)
        
    for i in range(10):
        print(hash_table[i])