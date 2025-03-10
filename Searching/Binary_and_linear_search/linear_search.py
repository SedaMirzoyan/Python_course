#in case of duplicates it will find the first one and return

def linear_search(arr, elem):
    found = False
    index = 0
    for i in arr:
        index += 1
        if (i == elem):
            found = True
            break

    if(found == False):
        print(f"Element {elem} not found")
    else:
        print(f"Element {elem} found at {index - 1}th index")
    return found

arr = [6, 7, 5, 9, 2, 1, 10, 7, 15]
elem1 = 2
elem2 = 3
print(linear_search(arr, elem1))
print(linear_search(arr, elem2))