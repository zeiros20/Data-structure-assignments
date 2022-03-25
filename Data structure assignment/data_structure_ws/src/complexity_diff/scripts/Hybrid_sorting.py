
from selection_script import selection_sort
from Merge_script import merge



def hybrid_sort(arr,threshold):
    if len(arr)<= threshold:
        selection_sort(arr)
        return arr
    middle = len(arr) // 2
    left_list = arr[:middle]
    right_list = arr[middle:]

    left_list = hybrid_sort(left_list,threshold)
    right_list = hybrid_sort(right_list,threshold)
    return list(merge(left_list, right_list))
    
        


arr = [2,6,7,1,5,25,3]
print(hybrid_sort(arr,3))
