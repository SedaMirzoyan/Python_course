
def join_middle(bound_by, tag_name):
    middle = int(len(bound_by)/2)
    middle_str = bound_by[0:middle] + tag_name + bound_by[middle:len(bound_by)] 
    return middle_str


bound_by1 = "[[]]"
tag_name1 = "tag"
print(join_middle(bound_by1, tag_name1))

bound_by2 = "<>"
tag_name2 = "body"
print(join_middle(bound_by2, tag_name2))