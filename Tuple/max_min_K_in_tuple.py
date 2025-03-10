#find the size of the tuple, min and max K elements 

def find_max_min_K_elems(input_tuple, k):
    count = 0
    to_list = list(input_tuple)

    #for max k elements
    while(count < k):
        data_max = max(to_list)
        yield data_max
        to_list.remove(data_max)
        #print(to_list)
        count += 1

    #for min k elements
    count = 0
    while(count < k):
        data_min = min(to_list)
        yield data_min
        to_list.remove(data_min)
        count += 1
    


def core(input_tuple, k):
    to_list = []

    data = find_max_min_K_elems(input_tuple, k)
    for i in data:
         to_list.append(i)

    out = tuple(to_list)

    return out


def main():
    tuple1 = (3, 7, 1, 18, 9, 22, 10, 56, 45, 0, -8)

    #find the size of tuple
    print(len(tuple1))

    tuple2 = (3, 7, 1)

    print(core(tuple1, 3))
    print(core(tuple2, 1))


if __name__ == "__main__":
    main()

