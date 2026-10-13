class Student:
    def __init__(self, name, id,):
        self.name = name
        self.id = id
        self.grade = []
    def add_grade(self, grade):
        self.grade.append(grade)
    def display_info(self):
        print("name:", self.name)
        print("id:", self.id)
        print("grade:", self.grade)
student1 = Student("karim",2500781, 70)
student2 = Student("mohamed", 2500987, 90)
student3 = Student("ahmed", 2500987, 80)

student1.display_info()
student2.display_info()
student3.display_info()