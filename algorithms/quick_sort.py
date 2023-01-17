import random

def quick_sort1(L, left = 0, right = None):
    if right is None:
        right = len(L) - 1
    if right - left > 0:
        pivot = partition1(L, left, right)
        
        quick_sort1(L, left, pivot-1)
        quick_sort1(L, pivot+1, right)
        
    return L
        
def partition1(L, left, right):
    pivot = right
    i = left
    j = pivot - 1
    
    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while i < j and L[j] >= L[pivot]:
            j -= 1
            
        if i < j:
            L[i], L[j] = L[j], L[i]
    
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot


def quick_sort2(L, left = 0, right = None):
    if right is None:
        right = len(L) - 1
    if left < right:
        pivot = partition2(L, left, right)
        quick_sort2(L, left, pivot-1)
        quick_sort2(L, pivot+1, right)
    return L

def partition2(L, left, right):
    pivot = left
    swap = pivot
    for i in range(pivot+1, right+1):
        if L[i] < L[pivot]:
            swap += 1
            L[i], L[swap] = L[swap], L[i]
    L[pivot], L[swap] = L[swap], L[pivot]
    
    pivot = swap
    return pivot


def randomized_quick_sort(L, left = 0, right = None):
    if right is None:
        right = len(L) - 1
    if right - left > 0:
        pivot = randomized_partition(L, left, right)
        
        randomized_quick_sort(L, left, pivot-1)
        randomized_quick_sort(L, pivot+1, right)
        
    return L

def randomized_partition(L, left, right):
    rand_pivot = random.randint(left, right)
    L[rand_pivot], L[right] = L[right], L[rand_pivot]
    return partition1(L, left, right)                       # calls the partition1 function


lst1 = [6, 3, 0, 1, 5, 2, 4]
lst2 = [4, 0, 1, 5, 2, 6, 3]
lst3 = [2, 5, 1, 6, 3, 4, 0]

print(quick_sort1(lst1))
print(quick_sort2(lst2))
print(randomized_quick_sort(lst3))