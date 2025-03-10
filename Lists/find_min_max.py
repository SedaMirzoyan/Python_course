def find_min(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if(arr[i] < min):
            min = arr[i]
    return min

def find_max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if(arr[i] > max):
            max = arr[i]
    return max


arr =  [3, -2, 1, 56, 10000, 167, -5, 25]
print(find_min(arr))
print(find_max(arr))