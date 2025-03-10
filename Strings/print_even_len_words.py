def print_even_len_words(input_string):
    to_list = input_string.split()
    out_list = []

    for i in to_list:
        print(i)
        if (len(i) % 2 == 0):
            out_list.append(i)

    return out_list


input_string = "Hii to everyone, this is a Python language"
print("String length is", len(input_string))
print(print_even_len_words(input_string))