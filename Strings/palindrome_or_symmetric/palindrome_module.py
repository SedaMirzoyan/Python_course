def if_palindrome(input_str):
    len_str = len(input_str)

    if len_str == 1:
        return True
    flag = False
    for i in range(0, int(len_str/2) ):
        j =  len_str - i - 1             
        if (i < j and input_str[i] == input_str[j]):
            flag = True
            j -= 1
        else:
            flag = False

    if(flag == True):
        print(f"{input_str} string is palindrome")
             
    return flag


