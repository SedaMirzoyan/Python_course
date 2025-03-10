
def reverse_words(input_str):
    temp = input_str.strip()
    str_list = temp.split()
    str_list.reverse()
    output_str = " ".join(str_list)

    print(output_str)

input_str = " I like this program very much "
reverse_words(input_str)