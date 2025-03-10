#create empty class
class Empty_class:
    pass

empty_obj = Empty_class()
print(empty_obj)
empty_obj.num = 35
print(empty_obj.num)


#Sorting objects of user defined class
class Numbers:
    def __init__(self, other):
        self.num = other

    def __lt__(self, other):
        return self.num < other.num
     
    def __gt__(self, other):
        return self.num > other.num
        
    def __eq__(self, other):
        return self.num == other.num
            
    def __le__(self, other):
        return self.num <= other.num
            
    def __ge__(self, other):
        return self.num >= other.num
    
    def __repr__(self):
        return f'Student({self.num})'


    
#ob = Student(56)
#obj = Student(24)
#print(ob > obj)

test_list = [Numbers(56), Numbers(12), Numbers(-9), Numbers(3), Numbers(23)]
print(sorted(test_list))
