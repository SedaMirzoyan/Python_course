
def bubble_sort(arr):
    sorted = False
    for i in range(0, len(arr)):
        sorted = False
        for j in range(0, len(arr) - i - 1):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                sorted = True
        if(sorted == False):
            break
            


input_arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]
bubble_sort(input_arr)
print(input_arr)