
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while((j >= 0) and (arr[j] > temp)):
            arr[j+1] = arr[j]
            j -= 1
        temp_swp = arr[j+1] 
        arr[j+1] = temp
        temp = temp_swp

    return arr
        

input_arr = [45, -6, 15, 2, 3, -2, 23, 17, 15, 5]
insertion_sort(input_arr)
print(input_arr)