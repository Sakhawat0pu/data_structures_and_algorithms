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
            
    def add_first(self, item):
        new_node = Node(item, self._head)
        if len(self) == 0:
            self._head = self._tail = new_node
        else:
            self._head = new_node
        self._length += 1
    
    def add_last(self, item):
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
        
    def remove_last(self):
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
    