def num_cube(input_list):
    out = []
    cube = 1
    for i in input_list:
        data = i
        cube = i*i*i
        elem = (data, cube)
        out.append(elem)
    
    return out


test_list = [1, 2, 3, 4, 5]
print(num_cube(test_list))