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

    def delete_value(self, value):
        if self is None:
            raise KeyError(f"{value} does not exist in the BST")
        elif value < self._value:
            if self._left:
                self._left = self._left.delete_value(value)
            else:
                raise KeyError(f"{value} does not exist in the BST")
        elif value > self._value:
            if self._right:
                self._right = self._right.delete_value(value)
            else:
                raise KeyError(f"{value} does not exist in the BST")
        else:
            if self._left == None and self._right == None:
                self = None
            elif self._left == None:
                self = self._right
            elif self._right == None:
                self = self._left
            else:
                right_subtree_min = self._right.min_value()
                self._value = right_subtree_min
                self._right.delete_value(right_subtree_min)
        return self
    
    def min_value(self):
        current_node = self
        while current_node._left is not None:
            current_node = current_node._left
        return current_node._value
            
    def contains(self, value):
        if self is None:
            return False
        elif self._value == value:
            return True
        elif self._value > value:
            if self._left:
                return self._left.contains(value)
            else:
                return False
        else:
            if self._right:
                return self._right.contains(value)
            else:
                return False
        
if __name__ == "__main__":
    values = [13, 22, 28, 45, 5, 27, 35, 8]
    bst = BinarySearchTree(25)
    for j in values:
        bst.insert_value(j)
    value = 35
    assert bst.contains(value) == True
    print(f"{value} is in binary search tree")        
    value = 88
    assert bst.contains(value) == False
    print(f"{value} is not in binary search tree") 
    value = 5
    bst.delete_value(value)
    print(f"Deleting {value} from the BST")
    assert bst.contains(value) == False
    print(f"{value} is not in binary search tree anymore") 
    value = 8
    assert bst.contains(value) == True
    print(f"{value} is in binary search tree") 

# if we had a Node class (contains value variable) and BinarySearchTree class had variable called root instead of value

#class Node:
#   def __init__(self, value):
#       self.value = value

#class BinarySearchTree:
#   def __init__(self):
#       self._root = Node(value)
#       self._right = None
#       self._left = None

    #def delete_node(self, value):
    #   self._delete_node(self._root, value)

    #def _delete_node(self, current_node, value):
    #   if current_node is None:
    #       raise KeyError(f"{value} does not exist in the binary tree")
    #   elif value < current_node.value:
    #       current_node._left = self._delete_node(current_node._left, value)
    #   elif value > current_node.value:
    #       current_node._right = self._delete_node(current_node._right, value)
    #   else:
    #       if current_node._left == None and current_node._right == None:
    #           current_node = None
    #       elif current_node._left == None:
    #           current_node = current_node._right
    #       elif current_node._right == None:
    #           current_node = current_node._left
    #       else:
    #           right_subtree_min_value = self.min_value(current_node.right)
    #           current_node.value = right_subtree_min_value
    #           current_node._right = self._delete_node(current_node.right, right_subtree_min_value)
    #   return current_node


    #def min_value(self, current_node):
    #   while current_node._left is not None:
    #       current_node = current_node._left
    #   return current_node.value