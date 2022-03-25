def partition(arr, l, h):
    lastS1 = l
    first = l+1
    while first <= h:
        if arr[first] < arr[l]:
            lastS1 += 1
            arr[first], arr[lastS1] = arr[lastS1], arr[first]
        first += 1
    arr[l], arr[lastS1] = arr[lastS1], arr[l]
    return lastS1

def kth_smallest(arr, l, h, k):
    if l < h:
        j = partition(arr, l, h)
        if j == k-1:
            print('Kth Smalles Number is:  ', arr[j])
            return
        if k == len(arr) and j == len(arr)-2 and arr[len(arr)-1] > arr[j]:
            print('Kth Smalles Number is:  ', arr[j+1])
            return
        if j > k-1:
            kth_smallest(arr ,l, j, k)   
        else:
            kth_smallest(arr, j+1, h, k)