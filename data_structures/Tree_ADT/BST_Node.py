import math

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.weight = 1
        
    def update_weight(self):
        left_w = self.left.weight if self.left else 0
        right_w = self.right.weight if self.right else 0
        self.weight = 1 + left_w + right_w
        return left_w, right_w
    
    def put(self, key, value, parent = None):
        if self.key == key:
            self.value = value
        elif self.key > key:
            if self.left:
                self.left.put(key, value, self)
            else:
                self.left = BSTNode(key, value)
        elif self.key < key:
            if self.right:
                self.right.put(key, value, self)
            else:
                self.right = BSTNode(key, value)
        
        left_w, right_w = self.update_weight()
        
        if (max(left_w, right_w) + 1) / (min(left_w, right_w) + 1) >= 3:
            if left_w < right_w:
                print(f"Rotating {self.key} to the left.")
                return self.rotate_left(parent)
            if left_w > right_w:
                print(f"Rotating {self.key} to the right")
                return self.rotate_right(parent)
        return self
    
    def get(self, key):
        if self.key == key:
            return self
        elif self.key > key:
            if self.left:
                return self.left.get(key)
        elif self.key < key:
            if self.right:
                return self.right.get(key)
        else:
            raise KeyError(f"Key {self.key} is not in the BST.")
    
    # rotate a node to the left if the right subtree is heavier than left subtree
    def rotate_left(self, parent):
        old, new = self, self.right
        old.right = new.left
        new.left = old
        
        old.update_weight()
        new.update_weight()
        
        if parent:
            print()
            is_left = old.key < parent.key
            if is_left:
                parent.left = new
            else:
                parent.right = new
        return new
    
    # rotate a node to the right if the left subtree is heavier than the right subtree
    def rotate_right(self, parent):
        old, new = self, self.left
        old.left = new.right
        new.right = old
        
        old.update_weight()
        new.update_weight()
        
        if parent:
            is_left = old.key < parent.key
            if is_left:
                parent.left = new
            else:
                parent.right = new
        return new
    
    def floor(self, key):   # find a value that is equal to key or the largest value in the BST that is less than key
        if self.key == key:
            return self
        elif self.key > key:
            if self.left:
                return self.left.floor(key)
            else:
                return None
        elif self.key < key:
            if self.right:
                temp_key = self.right.floor(key)
                if temp_key:
                    return temp_key
                else:
                    return self
            else:
                return self

    def ceil(self, key):    # find a value that is equal to key or the smallest value in the BST that is greater than key
        if key == self.key:
            return self
        elif key < self.key:
            if self.left:
                ceil = self.left.ceil(key)
                return ceil if ceil is not None else self
            else:
                return self
        elif key > self.key:
            if self.right:
                return self.right.ceil(key)
            else:
                return None
    
    def print_subtree(self):
        # lines is a list of lists: each sublist contains
        # a string corresponding to a line to be printed
        lines = self._print_subtree(lines=None)
        lines = [line for line in lines if (line and not line.isspace())]
        # use the string "join" method to join all objects in
        # an iterable with a separator.
        return "\n".join(lines)

    def _print_subtree(self, current_depth=None, lines=None, max_depth=None, w=None):
        # initialize variables the first time this is called
        if lines is None:
            height = math.floor(
                math.log2(self.weight)) + 2  # max height to draw. You can increase this to draw more unbalanced trees
            n_bottom = 2 ** height
            n_levels = height + 1  # levels in tree
            n_lines = 3 * n_levels  # lines to print tree
            w = 2 * n_bottom + 2 * n_bottom / 2 + 2 * (n_bottom / 2 - 1)  # calculate width of bottom level
            w = 2 ** math.ceil(math.log2(w))  # round w to a power of 2

            lines = ["" for i in range(n_lines)]  # lines to print

            max_depth = height - 1
            current_depth = 0  # initialize current_depth

        n_items = 2 ** (current_depth)  # number of items possible on this level
        item_width = w // n_items  # width of an item's string at this level

        # append current node to this line
        if self.left and self.right:
            lines[current_depth * 3] += "{:02}".format(self.key).center(item_width // 2 - 2, "_").center(item_width)
        elif self.left:
            line = "  " + "_" * (item_width // 4 - 2) + "{:02}".format(self.key) + " " * (item_width // 4)
            lines[current_depth * 3] += line.center(item_width)
        elif self.right:
            line = " " * (item_width // 4) + "{:02}".format(self.key) + "_" * (item_width // 4 - 2) + "  "
            lines[current_depth * 3] += line.center(item_width)
        else:
            lines[current_depth * 3] += "{:02}".format(self.key).center(item_width)

        # recursively call on left and right children
        if self.left:
            lines[current_depth * 3 + 1] += " /".center(item_width // 2)
            lines[current_depth * 3 + 2] += "/ ".center(item_width // 2)
            self.left._print_subtree(current_depth + 1, lines, max_depth, w)
        else:
            # append blank lines for all possible left children
            for i in range(current_depth, max_depth + 1):
                for j in range(1, 4):
                    lines[i * 3 + j] += "".center(item_width // 2)

        if self.right:
            lines[current_depth * 3 + 1] += "\\ ".center(item_width // 2)
            lines[current_depth * 3 + 2] += " \\".center(item_width // 2)
            self.right._print_subtree(current_depth + 1, lines, max_depth, w)
        else:
            # append blank lines for all possible right children
            for i in range(current_depth, max_depth + 1):
                for j in range(1, 4):
                    lines[i * 3 + j] += "".center(item_width // 2)

        return lines
    
if __name__ == "__main__":
    pairs = [[11, 1], [1, 34], [5, 12], [22, 1], [32, 3], [15, 5], [40, 1], [7, 99], [20, 4]]
    
    tree = BSTNode(19, 3)
    for pair in pairs:
        print(pair[0], pair[1])
        tree.put(pair[0], pair[1])
    print(tree.print_subtree())