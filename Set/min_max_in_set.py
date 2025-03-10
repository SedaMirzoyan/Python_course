def find_max(input_set):
    max = float('-inf')
    for i in input_set:
        if(i > max):
            max = i
    return max


def find_min(input_set):
    min = float('inf')
    for i in input_set:
        if(i < min):
            min = i
    return min



input_set = { 34, -5, -8, 0, 56, 12, 0, 67, 4}
print(find_max(input_set))
print(find_min(input_set))