def if_palindrome(input_str):
    len_str = len(input_str)

    if len_str == 1:
        return True
    flag = False
    for i in range(0, int(len_str/2) ):
        j =  len_str - i - 1             
        if (i < j and input_str[i] == input_str[j]):
            #print(input_str[i], input_str[j])
            flag = True
            j -= 1
        else:
            flag = False
             
    return flag


input_list = [ "abba", "abc", "a", "acbca", "rotator", "pattern", "khokho" ]

for i in input_list:
    print(if_palindrome(i))