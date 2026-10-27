
class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.ID)


class GraduateStudent(Student):
    def __init__(self, name, ID, program_title):
        super().__init__(name, ID)
        self.program_title = program_title

    def display_info(self):
        super().display_info()
        print("Program:", self.program_title)


class UndergraduateStudent(Student):
    def __init__(self, name, ID, major):
        super().__init__(name, ID)
        self.major = major

    def display_info(self):
        super().display_info()
        print("Major:", self.major)


grad1 = GraduateStudent("Ali", 101, "AI")
undergrad1 = UndergraduateStudent("Sara", 102, "Engineering")

grad1.display_info()
print()
undergrad1.display_info()
