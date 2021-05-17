# constructor
class Student:
    roll: ""
    gpa: ""

    def __init__(self, roll, gpa):
        self.gpa=gpa
        self.roll=roll

    def display(self):
        print(f"Roll: {self.roll} gpa: {self.gpa}")

Rahim = Student(101,3.7)
Rahim.display()

