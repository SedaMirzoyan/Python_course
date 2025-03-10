def union_of_arrays(arr1, arr2):
    arr = arr1 + arr2
    union_set = set(arr)
    union_arr = list(union_set)
    #print(union_arr)
    arr_len = len(union_arr)
    
    return arr_len


arr1 = [1, 2, 3, 4, 5]
arr2 =  [1, 2, 3]
print(union_of_arrays(arr1, arr2))