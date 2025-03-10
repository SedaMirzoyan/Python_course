def check_if_anagram(input_str1, input_str2):
    if (len(input_str1) != len(input_str2)):
        print("Length is different, not anagram")
        return False
    
    char_dict1, char_dict2  = {}, {}
    count1, count2 = 0, 0

    for i in input_str1:
        count1 += 1
        if i in char_dict1.keys():
            char_dict1.update({i: char_dict1[i] + 1})
        else:
            char_dict1.update({i: count1})
        count1 = 0

    for i in input_str2:
        count2 += 1
        if i in char_dict2.keys():
            char_dict2.update({i: char_dict2[i] + 1})
        else:
            char_dict2.update({i: count2})
        count2 = 0

    #print(char_dict1, char_dict2)
    if (char_dict1 == char_dict2):
        return True
    else:
        return False
 
    
print(check_if_anagram("tic", "tac"))
print(check_if_anagram("cat", "tac"))
print(check_if_anagram("knee", "keen"))
print(check_if_anagram("cat", "ccat"))
print(check_if_anagram("g", "g"))
#print(check_if_anagram("fuuuunnyy", "nunnyynnn"))   #for testing dictionaries
print(check_if_anagram("funny", "nunny"))