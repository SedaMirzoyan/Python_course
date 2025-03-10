def intersection_of_sorted_arrs(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    output_list = []

    for i in set1:
        for j in set2:
            if(i == j):
              output_list.append(i)  
    
    return output_list


arr1 = [1, 2, 3, 4, 1, 1, -9, 7]
arr2 = [2, 2, 4, 6, 7, 8, -9, 7, 7]
#arr1 = [1, 2, 3, 4, 5]
#arr2 = [6, 7, 8, -9, 7, 7]
print(intersection_of_sorted_arrs(arr1, arr2))