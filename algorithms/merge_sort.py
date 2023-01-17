def merge_sort1(L):
    if len(L) < 2:
        return
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]
    merge_sort1(left)
    merge_sort1(right)
    
    merge1(L, left, right)
    return L

def merge1(L, left, right):
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i+=1
        else:
            L[i+j] = right[j]
            j+=1
    L[i+j:] = left[i:] + right[j:]
    
lst1 = [6, 3, 0, 1, 5, 2, 4]
print(merge_sort1(lst1))

def merge_sort2(L):
    if len(L) == 1:
        return L
    mid = len(L) // 2
    left = merge_sort2(L[:mid])
    right = merge_sort2(L[mid:])
    
    return merge2(left, right)

def merge2(left, right):
    combined = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1
    combined[i+j:] = left[i:] + right[j:]
    return combined

lst2 = [4, 0, 1, 5, 2, 6, 3]
print(merge_sort2(lst2))

    

