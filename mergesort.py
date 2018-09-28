import random
def merge(arr, l, p, r):
    left = arr[l: p+1] #copy left part, including p
    right = arr[p+1: r+1] #copy right part, start from p+1
    i = 0
    j = 0
    k = l #start from the left
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(arr, l, r):
    if l < r:
        p = int((l + r) / 2)
        merge_sort(arr, l, p) #sort [1, p]
        merge_sort(arr, p+1, r) #sort[p + 1 ... end]
        merge(arr, l, p, r)
    
