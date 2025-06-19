class Student:
    students = []
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        Student.students.append(self)
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}") 
    
    def update_marks(self,new_marks):
        self.marks = new_marks
        print(f"Updated Marks for {self.name}: {self.marks}")
    
    @staticmethod
    def grade_from_marks(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"

        
    @classmethod
    def tot_stud(cls):
        print(f"Total number of students: {len(Student.students)}")

    @classmethod
    def class_avg(cls):
        if len(Student.students) == 0:
            print("No students to calculate average.")
            return
        else:
            tot_marks = sum(students.marks for students in cls.students) 
            avg = tot_marks / len(cls.students)
            return avg
    
    def isTopper(self):
        if self.marks >= 95:
            return True
        else:
            return False
        
class Topper(Student):
    def __init__(self, name, age, marks):
        super().__init__(name, age, marks)
    
    def display_info(self):
        print(f"Topper - Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

