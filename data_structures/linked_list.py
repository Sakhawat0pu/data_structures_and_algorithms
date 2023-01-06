import sys

class Node:
    def __init__(self, item, next = None):
        self._item = item
        self._next = next

class Linked_list:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        
    def __len__(self):
        return self._length
    
    def __str__(self):
        if len(self) == 0:
            return ''
        linked_list = []
        self._str(self._head, linked_list)
        return ''.join(linked_list)
    
    def _str(self, node , linked_list):
        if node._next is None:
            linked_list.append(str(node._item))
            return
        else:
            self._str(node._next, linked_list)
        linked_list.insert(0, str(node._item)+'-')
        
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
            
    def add_first(self, item):                      # Prepend
        new_node = Node(item, self._head)
        if len(self) == 0:
            self._head = self._tail = new_node
        else:
            self._head = new_node
        self._length += 1
    
    def add_last(self, item):                      # Append
        if len(self) == 0:
            self.add_first(item)
        else:
            new_node = Node(item)
            self._tail._next = new_node
            self._tail = self._tail._next
            self._length += 1
            
    def remove_first(self):
        if len(self) == 0:
            raise RuntimeError("Cannot remove from an empty collection!!")
        else:
            item = self._head._item
            removed_node = self._head
            if len(self) == 1:
                self._head = self._tail = None
            else:
                self._head = self._head._next
                removed_node._next = None
            self._length -= 1
            return item
        
    def remove_last(self):                      # Remove last
        if len(self) == 0:
            raise RuntimeError("Cannot remove from an empty collection!!")
        else:
            if len(self) == 1:
                return self.remove_first()
            else:
                item = self._tail._item
                tail = self._head
                while tail._next._next is not None:
                    tail = tail._next
                self._tail = tail
                self._tail._next = None
                self._length -= 1
                return item
    
    def get_item(self, index):
        if (index < 0) or (index >= len(self)):
            raise IndexError("Index out of range!!")
        else:
            temp = self._head
            for _ in range(index):
                temp = temp._next
            return temp._item
    
    def set_item(self, index, item):
        if (index < 0) or (index >= len(self)):
            raise IndexError("Index out of range!!")
        else:
            temp = self._head
            for _ in range(index):
                temp = temp._next
            temp._item = item
            
    def insert_item(self, index, item):
        if (index < 0) or (index >= len(self)):
            raise IndexError("Index out of range!!")
        elif (index == 0):
            self.add_first(item)
        elif (index == len(self)):
            self.add_last(item)
        else:
            temp = self._head
            for _ in range(index-1):
                temp = temp._next
            new_node = Node(item, temp._next)
            temp._next = new_node
            self._length += 1
    
    def remove_item(self, index):
        if (index < 0) or (index >= len(self)):
            raise IndexError("Index out of range!!")
        elif (index == 0):
            self.remove_first()
        elif (index == len(self)):
            self.remove_last()
        else:
            temp = self._head
            for _ in range(index-1):
                temp = temp._next
            pre = temp._next
            item = pre._item
            temp._next = pre._next
            pre._next = None
            self._length -= 1
            return item
        
if __name__ == "__main__":
    n = 10
    if len(sys.argv):
        n = int(sys.argv[1])
        
    ll = Linked_list()
    for i in range(n):
        ll.add_first(i)
    print(ll)
    print()
    for i in range(n):
        assert len(ll) == n - i
        ll.remove_first()
    print("Stack is working...")    # By adding first and removing first or by adding last and removing last in LL, we can implement Stack in LL
                                    # By adding first and removing last or by adding last and removing first in LL, we can implement Queue in LL
    
            
    ll1 = Linked_list()
    for i in range(n):
        ll1.add_first(i)
    for i in range(n):
        assert len(ll1) == n - i
        ll1.remove_last()
    print()
    print("Queue is also working...")
    
    print()
    for i in range(n):
        ll.add_last(i)
    print(ll)
    print()
    ll.set_item(5, 100)
    print(ll)
    print(ll.get_item(5))
    
    ll.insert_item(6, 101)
    print(ll)
    print(ll.remove_item(6))