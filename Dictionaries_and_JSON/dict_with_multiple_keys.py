#make dictionary with multiple inputs
#in below code keys are tuples and values are the sum of tuple elements

def make_dict(*args):
    out_dict = {}
    temp_dict = {}

    for i in range(0,len(args)):
        val = 0
        for j in range(0,len(args[i])):
            val += args[i][j]
            key = args[i]
            temp_dict.update({key:val})
        out_dict.update(temp_dict)

    return out_dict


print(make_dict((10, 20, 30),(5, 2, 4),(9, 10, 3)))
