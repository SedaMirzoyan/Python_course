stud_list = []

class Student:
    def __init__(self, name, rollno, marks1, marks2):
        self.name = name
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2

    
    def accept(self, name, rollno, marks1, marks2):
        stud_obj = Student(name, rollno, marks1, marks2)
        stud_list.append(stud_obj)

        return stud_list
    

    def display(self, stud_obj):
        print(f"{stud_obj.name}, {stud_obj.rollno}, {stud_obj.marks1}, {stud_obj.marks2}")
 

    
    def search(self, rollno):
        for ind in range(len(stud_list)): 
            if (stud_list[ind].rollno == rollno):
                print(f"Student with roll number {rollno} was found")
                return ind



    def delete(self, rollno):
        ind = self.search(rollno)
        stud_list.pop(ind)
        print(f"Student's info was deleted")



    def update(self, rollno_old, rollno_new):
        ind = self.search(rollno_old)
        stud_list[ind].rollno = rollno_new
        print("Roll number was updated")



obj = Student('', 0, 0, 0)  #object with default parameters

obj.accept("Alex", 1, 90, 95),
obj.accept("Brad", 2, 80, 76)
obj.accept("Jackson", 3, 100, 100),
obj.accept("Andy", 4, 65, 90),
obj.accept("Olivia", 5, 75, 81)
    
obj.search(2)

for i in range(len(stud_list)):
    obj.display(stud_list[i])

obj.delete(2)
obj.update(3,4)

for i in range(len(stud_list)):
    obj.display(stud_list[i])