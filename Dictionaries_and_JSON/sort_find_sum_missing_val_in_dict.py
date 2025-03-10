#sort dictionary keys
def sort_keys(input_dict):
    items_tuple = ()
    tuples_list = []

    for k, v in input_dict.items():
        items_tuple = (k, v)
        tuples_list.append(items_tuple)

    tuples_list.sort()
    #for i, j in tuples_list:
    #    print(f"i = {i}, j = {j}")

    output_dict = dict((item1, item2) for (item1, item2) in tuples_list)

    return output_dict


#handle missing keys
def find_missing_keys(input_dict):
    sorted_dict = sort_keys(input_dict)
    dict_keys_list = list(sorted_dict)

    for j in range(1, len(dict_keys_list)):
        diff = dict_keys_list[j] - dict_keys_list[j-1] 
        if (diff != 1):
            print(f" Dictionary key {dict_keys_list[j-1]+1} is missing")

    return sorted_dict
    


#find sum of all values in dictionary
def find_sum(input_dict):
    sum = 0
    for i in input_dict.values():
        sum += i
    return sum



def main():
    input_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, "aadish": 14, "sujit": 2}

    #print the size of the dictionary
    print("Dictionary length is", len(input_dict))

    print("sum is:", find_sum(input_dict))
    print(sort_keys(input_dict))

    input_dict_missing_keys = { 1: 'ravi', 2: 'rajnish', 3: 'ajay', 5: 'sanjeev', 7: "aadish", 8: "sujit", 10: "garima" }
    print(find_missing_keys(input_dict_missing_keys))


if __name__ == "__main__":
    main()

