from BST_Node import BSTNode


class BSTMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root:
            self.root = self.root.put(key, value)   # since self.root is BSTNode object here put() is the method from BSTnode [not recursion]
        else:
            self.root = BSTNode(key, value)

    def get(self, key):
        if self.root:
            return self.root.get(key).value         # since self.root is BSTNode object here get() is the method from BSTnode [not recursion]
        raise KeyError(f"key {key} not found in the Tree.")

    def floor(self, key):
        if self.root:
            floor_Node = self.root.floor(key)         # since self.root is BSTNode object here floor() is the method from BSTnode [not recursion]
            if floor_Node:
                return floor_Node.key, floor_Node.value
            else:
                return None, None

    def ceil(self, key):
        if self.root:
            ceil_Node = self.root.ceil(key)
            if ceil_Node:
                return ceil_Node.key, ceil_Node.value
            else:
                return None, None

    def __str__(self):
        if self.root:
            return self.root.print_subtree()
        else:
            return "Empty BST"


if __name__ == "__main__":
    n = 4
    s = BSTMap()
    for i in [2, 1, 3, 4, 5]:
        s.put(i, str(i))
        # print(s)
    for i in range(1, 6):
        assert s.get(i) == str(i)

    print("Everything is working completely fine")