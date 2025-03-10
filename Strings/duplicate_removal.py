def remove_duplicates(input_str):
    char_dict = {}
    count = 0

    for i in input_str:
        count += 1
        if i in char_dict.keys():
            char_dict.update({i: char_dict[i] + 1})
        else:
            char_dict.update({i: count})
        count = 0

    print(char_dict)

    to_list = list(input_str)
    to_list.reverse() #for last element index

    for k, v in char_dict.items():
        if (v > 1):
            #index = input_str.rfind(k)  
            index = to_list.index(k)
            to_list.pop(index)

    to_list.reverse()
    output_str = "".join(to_list)

    return output_str

    

input_str1 = "geEksforGEeks"
input_str2 = "HaPpyNewYear"
print(remove_duplicates(input_str1))
print(remove_duplicates(input_str2))