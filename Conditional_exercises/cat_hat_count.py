def cat_hat(str_input):
    count_hat, count_cat = 0, 0
    for i in range(0, len(str_input)):
        if (str_input[i:i+3] == 'hat'):
            count_hat += 1
        if (str_input[i:i+3] == 'cat'):         
            count_cat += 1

    print("count hat:", count_hat, "count cat:", count_cat)
    if ((count_hat == count_cat)):
        print("Cat and hat words appear same number of times")
        return True
    else:
        print("Cat and hat words appear different number of times")
        return False

input_list = [ "catinahat", "dogandcat", "dogandcatandmouse", "redhatcat", "redhat", "redblue" ]

for i in input_list:
    print(i, cat_hat(i))



