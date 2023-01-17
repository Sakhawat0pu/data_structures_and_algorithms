# bubble sort's running time O(n^2), selection sort's running time O(n^2)
# and insertion sort's running time O(n) [if the list is almost sorted] or  O(n^2)
# Merge sort's average running time O(nlog(n)) and quick sort's average
# running time O(nlog(n)) and worst case running time O(n^2) [if the list is almost sorted or sorted in reversed]
# running time of quickselect is O(n).
# space complexity of bubble, insertion, selection sort is 0(1)
# space complexity of merge and quick sort is 0(n)
# running time of binary search using slicing is O(n) and without using
# slicing is O(log(n))..


# the following function check if a list is sorted in ascending manner

def is_sorted(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

# find the smallest element of the list and put it at the front of the list
def bubble_sort1(L):
    n = len(L)
    for i in range(n-1):
        for j in range(i+1, n):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L
                

# find the biggest item and put it at the back of the list
def bubble_sort2(L):
    n = len(L)
    for i in range(n-1):
        for j in range(n-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L
            
def bubble_sort3(L):
    n = len(L)
    keep_going = True
    while keep_going:
        keep_going = False
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                keep_going = True
    return L

lst1 = [6, 3, 0, 1, 5, 2, 4]
lst2 = [4, 0, 1, 5, 2, 6, 3]
lst3 = [2, 5, 1, 6, 3, 4, 0]

print(bubble_sort1(lst1))
print(bubble_sort2(lst2))
print(bubble_sort3(lst3))