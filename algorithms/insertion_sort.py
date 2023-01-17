def insertion_sort1(L):
    n = len(L)
    for i in range(n):
        j = i
        k = i - 1
        while L[k] > L[j] and k >= 0:
            L[k], L[j] = L[j], L[k]
            j -= 1
            k -= 1
    return L

def insertion_sort2(L):
    n = len(L)
    for i in range(n-1):
        for j in range(n-2-i, n-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            else:
                break
    return L

def insertion_sort3(L):
    n = len(L)
    for i in range(n-1):
        j = n - 2 - i
        while j < n - 1 and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j += 1
    return L

lst1 = [6, 3, 0, 1, 5, 2, 4]
lst2 = [4, 0, 1, 5, 2, 6, 3]
lst3 = [2, 5, 1, 6, 3, 4, 0]


print(insertion_sort1(lst1))
print(insertion_sort2(lst2))
print(insertion_sort3(lst3))