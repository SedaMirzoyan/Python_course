def row_wise_addition(input_list, cus_eles):
    out_list = []
    
    for i, elem in enumerate(cus_eles):
        temp_list = []
        for tuple_elem in input_list[i]:
            new_tuple = list(tuple_elem)
            new_tuple.append(elem)
            temp_list.append(tuple(new_tuple))
        out_list.append(temp_list)

    return out_list


test_list = [[('Gfg', 3), ('is', 3)], 
             [('best', 1)], 
             [('for', 5), ('geeks', 1)]]
cus_eles = [6, 7, 8] 
print(row_wise_addition(test_list, cus_eles))