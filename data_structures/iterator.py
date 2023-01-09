class Stack:
    def __init__(self):
        self._L = []
    
    def push(self, value):
        self._L.append(value)
    
    def pop(self):
        return self._L.pop()
    
    def __iter__(self):
        return Stack_iterator(self)

class Stack_iterator:
    def __init__(self, s):
        self._s = s
        self.counter = len(self._s._L) - 1
        
    def __next__(self):
        while self.counter >= 0:
            next_item = self._s._L[self.counter]
            self.counter -= 1
            return next_item
        raise StopIteration
    
if __name__ == "__main__":
    s = Stack()
    n = 5
    for i in range(n):
        s.push(i)
    for j in s:
        print(str(j), end=" ")
    print()