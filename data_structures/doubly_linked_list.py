import sys

class Node:
    def __init__(self, item, prev = None, next = None):
        self._item = item
        self._prev = prev
        self._next = next

class Doubly_linked_list:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        
    def __len__(self):
        return self._length
    
    def __str__(self):
        if len(self) == 0:
            return ''
        item_list = []
        self._str(self._head, item_list)
        return ''.join(item_list)
    
    def _str(self, node , item_list):
        if node._next is None:
            item_list.append(str(node._item))
            return
        else:
            self._str(node._next, item_list)
        item_list.insert(0, str(node._item)+'-')
        
    def __contains__(self, item):
        if len(self) == 0:
            return False
        else:
            return self._in(self._head, item)
        
    def _in(self, node, item):
        if node is None:
            return False
        elif node._item == item:
            return True
        else:
            self._in(node._next, item)
            
    def add_first(self, item):                      # Append
        new_node = Node(item, None, self._head)
        if len(self) == 0:
            self._head = self._tail = new_node
        else:
            self._head._prev = new_node
            self._head = new_node
        self._length += 1
        
    def add_last(self, item):
        new_node = Node(item, self._tail, None)
        if len(self) == 0:
            self._head = self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node
        self._length += 1
    
    def remove_first(self):
        item = None
        if len(self) == 0:
            raise RuntimeError("Cannot remove item from an empty codllection!!")
        elif len(self) == 1:
            item = self._head._item
            self._head = self._tail = None
        else:
            item = self._head._item
            temp = self._head
            self._head = self._head._next
            self._head._prev = None
            temp._next = None
        self._length -= 1
        return item
    
    def remove_last(self):
        item = None
        if len(self) == 0 or len(self) == 1:
            return self.remove_first()
        else:
            item = self._tail._item
            temp = self._tail
            self._tail = self._tail._prev
            self._tail._next = None
            temp._prev = None
        self._length -= 1
        return item

    def get_item(self, index):                          # Returns the node at the index not the item at that index
        temp = self._head
        if index < 0 or index >= len(self):
            raise IndexError("index out of range!!")
        elif index < (len(self) / 2):
            for _ in range(index):
                temp = temp._next
        else:
            temp = self._tail
            for _ in range(len(self) - index - 1):
                temp = temp._prev
        return temp
    
    def set_item(self, index, item):
        temp = self.get_item(index)
        if temp:
            temp._item = item
            return True
        return False
    
    def insert_item(self, index, item):
        temp = self.get_item(index)
        if temp:
            before_temp = temp._prev
            new_node = Node(item, before_temp, temp)
            before_temp._next = new_node
            temp._prev = new_node
            self._length += 1
            return True
        return False
    
    def remove_item(self, index):

        if index < 0 or index >= len(self):
            raise IndexError("index out of range!!")
        elif index == 0:
            return self.remove_first()
        elif index == (len(self) - 1):
            return self.remove_last()
        else:
            temp = self.get_item(index)
            item = None
            if temp:
                item = temp._item
                before_temp = temp._prev
                after_temp = temp._next
                before_temp._next = after_temp
                after_temp._prev = before_temp
            
            self._length -= 1
            return item
        
    def reverse(self, mid = None):
        if (len(self) % 2) == 0:
            mid = int(len(self) / 2)
            is_inserted = self.insert_item(mid, 0)
            if is_inserted:
                self.reverse(mid)    
        else:
            first = self._head
            last = self._tail
            while first != last:
                first._item, last._item = last._item, first._item
                first = first._next
                last = last._prev

            if mid:
                self.remove_item(mid)
            return
        
if __name__ == "__main__":
    n = 10
    if len(sys.argv):
        n = int(sys.argv[1])
    dll = Doubly_linked_list()
    for i in range(n):
        dll.add_first(i)
    print(dll)
    
    for i in range(n):
        assert len(dll) == n - i
        dll.remove_first()
    print("Stack is working...")
    
    dll_1 = Doubly_linked_list()
    for i in range(n):
        dll_1.add_first(i)
    
    print()
    print(dll_1)
    
    for i in range(n):
        assert len(dll_1) == n - i
        dll_1.remove_last()
    
    print("Queue is also working...")
    print()
    
    dll_2 = Doubly_linked_list()
    for i in range(n):
        dll_2.add_last(i)
    print(dll_2)
    print(dll_2.remove_first())
    print(dll_2.remove_last())
    print(dll_2)
    print()
    
    node = dll_2.get_item(11)

    print(node._item)
    assert dll_2.set_item(11, 100) == True
    print("100 was set at index 11")
    print(dll_2)
    print()
    
    dll_2.insert_item(5, 99)
    print(dll_2)
    print()
    
    dll_2.remove_item(5)
    print(dll_2)
    print()
    dll_2.insert_item(11, 12)
    print(dll_2)
    dll_2.reverse()
    print(dll_2)