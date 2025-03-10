def sum(input_tuple):
    sum = 0
    for i in input_tuple:
        sum += i

    return sum

input_tuple = (7, 8, 9, 1, 10, 7)
print(sum(input_tuple))