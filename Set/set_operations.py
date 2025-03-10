#Implement set in Python


input_list = ["apple", "banana", "cherry", "orange"]
this_set = {"pear"}

#add more than one elements into set
this_set.update(input_list)
print(this_set)

#add one element into set
this_set.add("melon")
print(this_set)

#delete element from the set
this_set.remove("cherry")
print(this_set)

#remove random item
this_set.pop()
print(this_set)

#Returns the union of sets in a new set
set_veggie = {"tomato", "cucumber", "cabbage"}
set_join = this_set.union(set_veggie)
print("Set after union", set_join)

#Insert all items from one set into another
this_set.update(set_veggie)
print("Print set after update:", this_set)

#print sum of all elements of set
set_num = {3, -2, 17, 56, 49, -34, 12}
print("sum is", sum(set_num))

#length of a set
print(len(set_num))

#print new sorted list from elements in the sets
frozen_set_num = frozenset((set_num))
print(sorted(frozen_set_num))


#remove all elements from set
set_num.clear()
print("set_num after deleting:", set_num)