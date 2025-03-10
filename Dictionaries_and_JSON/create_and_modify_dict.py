#create dictionary
def create_dict(names, marks):
    stud_dict = dict(zip(names, marks))

    return stud_dict


#insert key, val into dict
def insert_dict(input_dict, input_elem): 
    input_dict.update(input_elem)
    print(f"{input_elem} was inserted")


#deleting key with corresponding input
def del_dict(input_dict, input_key):
    #use list(dict.keys()) for not getting "dict size was changed error",
    # for not to changing dict and break the keys iterator
    dict_orig_size = len(input_dict)
    for k in list(input_dict.keys()): 
        if(k == input_key):
            input_dict.pop(input_key)
            print(f"{input_key} was deleted")
            break

    if(dict_orig_size == len(input_dict)): 
        print("-1")


#print dict keys
def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f"Marks of student {k} is: {v}")


names  = ["john", "ala", "lilia", "sudan", "mercy"] 
marks = [100, 200, 150, 80, 300]

stud_dict = create_dict(names, marks)
print(stud_dict)

input_key = "mercy"
input_elem = {"james": 50}

insert_dict(stud_dict, input_elem)
print_dict(stud_dict)
del_dict(stud_dict, input_key)
print("after deleting:", stud_dict)