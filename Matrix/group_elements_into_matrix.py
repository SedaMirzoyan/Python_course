def group_elems(input_list):
   input_list.sort()
   count = 0
   data_dict = {}

   for i in input_list:
        count += 1
        if i in data_dict.keys():
            data_dict.update({i: data_dict[i] + 1})
        else:
            data_dict.update({i: count})
        count = 0
    
   out = [v * [k] for k, v in data_dict.items()]
   return out
    


test_list = [1, 3, 4, 4, 2, 3, 3] 
print(group_elems(test_list))