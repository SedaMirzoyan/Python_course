def find_last_match(input_str, pattern):
    for i in range(len(input_str)-1, 1, -1):
        ind = 0
        if (input_str[i] == pattern[0]):
            for j in range(0, len(pattern)):
                if(input_str[i:i+len(pattern)] == pattern[j:j+len(pattern)]):
                    ind = i + 1
                    break
            if (ind != 0):
                break

    return ind
                   

        
def find_pattern(input_str, pattern):
    if pattern in input_str:
        return True
    return False


def binary_search_iterative(arr, data):
    left = 0
    right = len(arr) - 1

    while(left < right):
        mid = int((left + right)/2)
        if data == arr[mid]:
            return mid
        elif(data < arr[mid]):
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


def binary_search_recursive(arr, data, left, right):
    mid = int((left + right)/2)
    if(left > right):
        return mid
    
    if(data not in arr):
        return -1
    
    if(data == arr[mid]):
        return mid
    elif(data < arr[mid]):
        return binary_search_recursive(arr, data, mid, mid-1)
    elif(data > arr[mid]):
        return binary_search_recursive(arr, data, mid+1, right)

    


def main():
    test_str = "abcdefh"
    pattern = "cde"
    print(find_pattern(test_str, pattern))

    test_str1 = "abcdefghijklghifghsd"
    pattern1 = "ghi"
    print(find_last_match(test_str1, pattern1))

    arr = [1, 2, 3, 4, 6, 7, 8, 11]
    data = 7
    left = 0
    right = len(arr) - 1
    print(binary_search_iterative(arr, data))
    print(binary_search_recursive(arr, data, left, right))

if __name__ == "__main__":
    main()
