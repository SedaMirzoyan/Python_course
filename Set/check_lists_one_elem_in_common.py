#Check if two lists have atleast one element common

def find_if_common(list1, list2):
    to_set1 = set(list1)
    to_set2 = set(list2)

    common = to_set1.intersection(to_set2)

    if(len(common) >= 1):
        print("Lists have atleast one common element")
        return True
    else:
        print("Lists don't have common element")
        return False
    

list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]
list3 = [1, 2, 7]

print(find_if_common(list1, list2))
print(find_if_common(list2, list3))