#Assigning Subsequent Rows to Matrix first row elements

def assign_rows(input_list):
    if (len(input_list) % 2 == 1):
        return -1
    
    out = {}
    for i in range(len(input_list)-1):
        #print(i)
        for j in range(len(input_list[0])):
            key = input_list[0][j] 
            val = input_list[i+1]
            out.update({key:val})

    return out


test_list = [[5, 8, 10],
            [2, 0, 9], 
            [5, 4, 2], 
            [2, 3, 9]] 

print(assign_rows(test_list))