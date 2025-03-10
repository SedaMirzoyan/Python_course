def remove_ith_char(input_string, i):
    to_list = list(input_string)
    to_list.pop(i)
    output_str = "".join(to_list)

    return output_str


input_string = "elephant"
print(remove_ith_char(input_string, 3))