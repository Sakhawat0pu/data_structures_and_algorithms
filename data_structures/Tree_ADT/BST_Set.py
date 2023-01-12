from bst_traversal import BSTNode 

class BSTSet:
    def __init__(self):
        self._root = None
    
    def put(self, key):
        if self._root:
            self._root.put(key)
        else:
            self._root = BSTNode(key)
    
    # classic iteration (bad)
    def __iter__(self):
        return iter(self._root)
    
    def in_order(self):
        if self._root: 
            yield from self._root.in_order()

    def pre_order(self):
        if self._root: 
            yield from self._root.pre_order()

    def post_order(self):
        if self._root: 
            yield from self._root.post_order()
    
if __name__ == "__main__":
    s = BSTSet()
    lst = [2, 1, 6, 7, 4, 3, 5]
    for i in lst:
        s.put(i)
        
    in_order = []
    for item in s.in_order():
        in_order.append(item)
    print(in_order)

    post_order = []
    for item in s.post_order():
        post_order.append(item)
    print(post_order)

            