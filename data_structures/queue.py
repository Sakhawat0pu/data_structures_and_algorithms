class Queue:
    def __init__(self):
        self._L = []
    
    def __len__(self):
        return len(self._L)
    
    def is_Empty(self):
        return len(self) == 0

    def enqueue(self, value):
        self._L.append(value)
    
    def dequeue(self):
        return self._L.pop(0)
    
    def peek(self):                     # peek returns the first item in the Queue
        return self._L[0]
    
if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    l1 = Queue()
    for i in range(n):
        l1.enqueue(i)
    
    for i in range(n):
        assert len(l1) == n - i
        print(l1.dequeue())
    
    print("Queue is working perfectly fine!!")