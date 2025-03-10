
def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub
    pivot_place = pivot
    temp = pivot

    while(start < end):
        while((arr[start] <= pivot) and (start < ub)):
            start = start + 1
        while((arr[end] > pivot) and (end > lb)):
            end = end - 1
        if (start < end):
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp  
    pivot_place = arr[lb]
    arr[lb] = arr[end]
    arr[end] = pivot_place

    return end



def quick_sort(arr, lb, ub):
    if (lb < ub):
        loc = partition(arr, lb, ub)
        quick_sort(arr, lb, loc - 1)
        quick_sort(arr, loc + 1, ub)



input_arr = [2, -6, 15, 5, -3, 2, 1, 17, 23, 45]
quick_sort(input_arr, 0, len(input_arr)-1)
print(input_arr)