def interchange_elems(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp


input_list = [1, 2, 3, 4, 5]
interchange_elems(input_list)
print(input_list)