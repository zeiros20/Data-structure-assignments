def insertion_sort(array):
  for i in range(1, len(array)):
    j = i
    nxt_element = array[i]
    while (array[j-1] > nxt_element) and (j > 0):
      array[j] = array[j-1]
      j=j-1
    array[j] = nxt_element
    
