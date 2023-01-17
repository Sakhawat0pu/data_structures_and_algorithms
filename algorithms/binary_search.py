# you need to provide binary_search a sorted list, otherwise the algorithm won't work

def binary_search(my_list, item):
    first = 0
    last = len(my_list) - 1
    mid = (first + last) // 2
    while mid >= first or mid < last:
        if my_list[mid] == item:
            return True
        elif my_list[mid] > item:
            last = mid - 1
            mid = (first + last) // 2
        else:
            first = mid + 1
            mid = (first + last)//2
    return False

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in L:
#     print(binary_search(L, i))
# print(binary_search(L, 20))

def binary_search_rec1(my_list, item, first, last):
    mid = (first + last) // 2
    if first > last:
        return False
    elif my_list[mid] == item:
            return True
    elif my_list[mid] > item:
        return binary_search_rec1(my_list, item, first, mid-1)
    else:
        return binary_search_rec1(my_list, item, mid+1, last)

# for i in L:
#     print(binary_search_rec1(L, i, 0, len(L)-1))
    
# print(binary_search_rec1(L, 11, 0, len(L)-1))

def binary_search_rec2(my_list, item):
    if len(my_list) == 0:
        return False
    mid = len(my_list) // 2
    if my_list[mid] == item: 
        return True
    elif my_list[mid] > item: 
        return binary_search_rec2(my_list[:mid], item)
    else: 
        return binary_search_rec2(my_list[mid+1:], item)
    
for i in L:
    print(binary_search_rec2(L, i))
    
print(binary_search_rec2(L, -1))