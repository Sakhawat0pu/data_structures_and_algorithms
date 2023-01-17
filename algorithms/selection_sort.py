def selection_sort1(L):
    n = len(L)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1, n):
            if L[min_ind] > L[j]:
                min_ind = j
        if min_ind != i:
            L[min_ind], L[i] = L[i], L[min_ind]
    return L    


def selection_sort2(L):
    n = len(L)
    for i in range(n-1):
        max_ind = 0
        for j in range(1, n-i):
            if L[j] > L[max_ind]:
                max_ind = j
        L[max_ind], L[n-1-i] = L[n-i-1], L[max_ind]
    return L        

lst1 = [6, 3, 0, 1, 5, 2, 4]
lst2 = [4, 0, 1, 5, 2, 6, 3]

print(selection_sort1(lst1))
print(selection_sort2(lst2))