class BSTNode:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        
    def put(self, key):
        if self._key == key:
            return
        elif self._key > key:
            if self._left:
                self._left.put(key)
            else:
                self._left = BSTNode(key)
        else:
            if self._right:
                self._right.put(key)
            else:
                self._right = BSTNode(key)
    
    # classical iteration (bad)
    def __iter__(self):
        return BST_iterator(self)
    
    # generator based iteration (good)
    def in_order(self):
        if self._left: yield from self._left.in_order()         # recursively go left
        yield self._key
        if self._right: yield from self._right.in_order()       # recursively go right
        
    def pre_order(self):
        yield self._key
        if self._left: yield from self._left.in_order()
        if self._right: yield from self._right.in_order()
    
    def post_order(self):
        if self._left: yield from self._left.in_order()
        if self._right: yield from self._right.in_order()
        yield self._key
    
    # Freebie! This will help you print out useful info on nodes, if you want
    def __repr__(self):
        return f"BSTNode(key = {self._key})"
# This technique is bad and slow, you shouldn't use it!
class BST_iterator:
    def __init__(self, node):
        self._L = []
        self._in_order(node)
        self._counter = 0
        
    def _in_order(self, node):
        if node.left: self._in_order(node._left)
        self._L.append(node)
        if node.right: self._in_order(node._right)
    
    def __next__(self):
        if self._counter < len(self._L):
            key = self._L[self._counter].key
            self._counter -= 1
            return key
        raise StopIteration
    
if __name__ == "__main__":
    tree = BSTNode(4)
    lst = [2, 1, 6, 7, 5]
    for item in lst:
        tree.put(item)

    in_ord = []
    for item in tree.in_order():
        in_ord.append(item)
    print("IN-ORDER")
    print(in_ord)

    pre_ord = []
    for item in tree.pre_order():
        pre_ord.append(item)
    print("PRE-ORDER")
    print(pre_ord)

    post_ord = []
    for item in tree.post_order():
        post_ord.append(item)
    print("POST-ORDER")
    print(post_ord)
