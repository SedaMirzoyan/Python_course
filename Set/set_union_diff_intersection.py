def all_in_set(set1, set2):
    out_set = set1.union(set2)
    return out_set
    

def common_in_set(set1, set2):
    out_set = set1.intersection(set2)
    return out_set


def diff(set1, set2):
    out_set = set1.difference(set2)
    return out_set   



set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 2, 3}
print(all_in_set(set1, set2))
print(common_in_set(set1, set2))
print(diff(set1, set2))
