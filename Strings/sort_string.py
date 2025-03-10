def sort_string(input_string):
    to_list = list(input_string)
    to_list.sort()
    output_str = "".join(to_list)

    return output_str


input_string = "edcab"
print(sort_string(input_string))