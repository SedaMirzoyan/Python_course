def repeat_string(str1, str2):
    max_len = len(str1)
    max_str = str1
    min_str = str2

    if (len(str2) > max_len):
        max_str = str2 
        min_str = str1
    
    output_str = min_str + max_str + min_str
    return output_str



str1 = "Hi"
str2 = "There"
print(repeat_string(str1, str2))