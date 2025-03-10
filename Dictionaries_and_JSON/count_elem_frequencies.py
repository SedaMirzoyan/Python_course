#counting element frequencies

def check_sum(arr, input_sum):
    sum = 0
    print(arr)
    dict_sum = {}

    for i in range(0, len(arr) - 1):
        sum = arr[i] + arr[i + 1]
        dict_sum[(arr[i], arr[i+1])] = sum
  
    print(dict_sum)
    for k, v in dict_sum.items():
        if (input_sum == v):
            print(f"Pair {k} with sum {input_sum} is present in the array")
            return True
    return False


arr1 = [1, 2, 3, 3, 5]
sum1 = 8
arr2 = [3, 2, 5]
sum2 = 6

print(check_sum(arr1, sum1))
print(check_sum(arr2, sum2))