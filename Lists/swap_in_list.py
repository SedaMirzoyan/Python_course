#swap third and penultimate elements in a list
def swap_elements(arr):
    temp = arr[2]
    arr[2] = arr[-2]
    arr[-2] = temp


input_list = [50, 20, 30, 40, 10, 60]
swap_elements(input_list)
print(input_list)