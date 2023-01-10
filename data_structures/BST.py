class BinarySearchTree:
    def __init__(self, value, right = None, left = None):
        self._value = value
        self._right = right 
        self._left = left
    
    def insert_value(self, value):
        if self._value == value:
            print("Value already exists. Duplicates not allowed!")
            return
        elif self._value > value:
            if self._left:
                return self._left.insert_value(value)    # called insert_value method on the left subtree [self._left replaces self on the next call]
            else:
                self._left = BinarySearchTree(value)    # if left subtree does not exist (None). Then we create a left subtree
                return
        else:
            if self._right:
                return self._right.insert_value(value)   # called insert_value method on the right subtree [self._right replaces self on the next call]
            else:
                self._right = BinarySearchTree(value)   # if right subtree does not exist (None). Then we create a right subtree
                return

    
    def contains(self, value):
        if self is None:
            return False
        elif self._value == value:
            return True
        elif self._value > value:
            return self._left.contains(value)
        else:
            return self._right.contains(value)
        
if __name__ == "__main__":
    values = [13, 22, 28, 45, 5, 27, 35, 8]
    bst = BinarySearchTree(25)
    for j in values:
        bst.insert_value(j)
    value = 45
    assert bst.contains(value) == True
    print(f"{value} is in binary search tree")        
    value = 88
    print(f"{value} is not in binary search tree") 