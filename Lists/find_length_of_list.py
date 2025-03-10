def find_length_built_in(arr):
    return len(arr)


def find_length_counter(arr):
    count = 0   
    for i in arr:
        count += 1

    return count


input_list = [1, 2, 3, 4, 5]
print(find_length_built_in(input_list))
print(find_length_counter(input_list))