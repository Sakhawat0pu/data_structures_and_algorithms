class Stack:
    def __init__(self):
        self._L = []
    
    def __len__(self):
        return len(self._L)
    
    def push(self, value):
        self._L.append(value)
    
    def pop(self):
        return self._L.pop()
    
    def peek(self):                     # peek returns the top item in the stack
        return self._L[-1]
    
    def is_Empty(self):
        return len(self) == 0

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    l1 = Stack()
    for i in range(n):
        l1.push(i)
    
    for i in range(n):
        assert len(l1) == n - i
        print(l1.pop())
    
    print("Stack is working perfectly fine!!")