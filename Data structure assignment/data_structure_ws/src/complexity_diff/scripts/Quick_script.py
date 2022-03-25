import numpy as np

def partition(arr, l, h):
    pivot_index = np.random.randint(l, h)
    if pivot_index == l:
        lastS1 = l
        first = l+1
    else:
        first = l
        lastS1 = l-1
    while first <= h:
        if arr[first] < arr[pivot_index]:
            lastS1 += 1
            if lastS1 == pivot_index:
                lastS1 += 1
            arr[first], arr[lastS1] = arr[lastS1], arr[first]
        first += 1
    if lastS1 < pivot_index:
        lastS1 += 1
    arr[pivot_index], arr[lastS1] = arr[lastS1], arr[pivot_index]
    return lastS1

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)