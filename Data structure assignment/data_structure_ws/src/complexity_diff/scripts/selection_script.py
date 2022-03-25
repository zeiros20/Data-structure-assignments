def selection_sort(array):
   list = array
   for indx in range(len(list)-1):
      min = indx
      for j in range(indx +1, len(list)):
         if list[min] > list[j]:
            min = j
      if indx!=min:
         list[indx], list[min] = list[min], list[indx]
