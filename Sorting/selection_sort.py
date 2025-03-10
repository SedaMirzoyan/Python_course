def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

    return arr

        
input_arr = [45, -6, 15, 2, 3, -2, 23, 17, 15, 8]
selection_sort(input_arr)
print(input_arr)


